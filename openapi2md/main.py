import json
import sys
import os
from string import Template
from collections import OrderedDict
import copy
from jsf import JSF


def read_spec_json(file_path: str):
    with open(file_path, "r") as spec_json:
        return json.load(spec_json)


def get_template(template_name: str):
    """
    Load template content, works both in development and PyInstaller binary.
    """
    if getattr(sys, "frozen", False):
        # Running inside PyInstaller binary
        base_path = sys._MEIPASS
        template_path = os.path.join(
            base_path, "openapi2md", "templates", f"{template_name}-template.mdx"
        )
    else:
        # Running from source
        template_path = os.path.join(
            os.path.dirname(__file__), "templates", f"{template_name}-template.mdx"
        )

    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def write_md(content: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as api_doc:
        api_doc.write(content)


def get_auth_format(schemes):
    return "".join(
        f"**`{key}`** _({scheme.get('type')}, {scheme.get('scheme')})_"
        for key, scheme in schemes.items()
    )


def get_request_content(request: dict, components: dict):
    if "content" in request:
        request_list = []
        content = request.get("content")
        request_template = Template(get_template("request"))
        for content_type, schema_ref in content.items():
            schema_def = resolve_ref(schema_ref, components)
            schema_json = JSF(schema_def.get("schema")).generate(n=1)
            request_content = request_template.substitute(
                content_type=content_type,
                schema_json=json.dumps(schema_json, indent=2),
            )
            request_list.append(request_content)
        return request_list
    return ["**`None`**"]


def get_response_content(responses: dict, components: dict):
    responses_list = []
    for status_code, response in responses.items():
        description = response.get("description")
        content = response.get("content", {})

        response_template = Template(get_template("response"))

        for content_type, content_json in content.items():
            schema = resolve_ref(content_json, components)
            for _, schema_def in schema.items():
                schema_json = JSF(schema_def).generate(n=1)
                response_content = response_template.substitute(
                    status_code=status_code,
                    description=description,
                    content_type=content_type,
                    schema_json=json.dumps(schema_json, indent=2),
                )

                responses_list.append(response_content)

    return responses_list


def get_path_content(paths, securitySchemes, base_url="", components={}):
    path_content_json = {}
    for path, path_info in paths.items():
        endpoint = f"{base_url}{path}"
        for method, method_info in path_info.items():
            for tag in method_info.get("tags", ["Default"]):
                security_schemes = ""
                for security in method_info.get("security", []):
                    for key, _ in security.items():
                        scheme = securitySchemes.get(key, {})
                        security_schemes += f"**`{key}`** _({scheme.get('type')}, {scheme.get('scheme')})_"
                security_schemes = "- Authorizations: " + (
                    security_schemes.strip() if security_schemes else "**`None`**"
                )

                request_body = method_info.get("requestBody", {})
                request_schemas = get_request_content(request_body, components)
                request_content = "**Request:** \n\n" + "\n".join(request_schemas)

                responses = method_info.get("responses", {})
                responses_schemas = get_response_content(responses, components)
                responses_content = "**Responses:** \n\n" + "\n".join(responses_schemas)

                summary = method_info.get("summary", "No summary provided")

                path_template = Template(get_template("path"))
                path_content = path_template.substitute(
                    endpoint=endpoint.strip(),
                    auths=security_schemes,
                    method=method.upper(),
                    summary=summary.strip(),
                    request=request_content,
                    response=responses_content,
                )
                path_content_json.setdefault(tag, []).append(path_content)

    combined_path_content = ""
    paths_template = Template(get_template("paths"))
    for tag, contents in path_content_json.items():
        paths_content = "".join(contents)
        combined_path_content += paths_template.substitute(
            tags=tag, paths=paths_content.strip()
        )

    return combined_path_content


def resolve_ref(schema: dict, components: dict):
    """Recursively resolve all $ref occurrences inside a JSON schema."""
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_path = schema["$ref"]
            # if ref_path.startswith("#/components/schemas/"):
            schema_name = ref_path.split("/")[-1]
            # deep copy to avoid mutation
            resolved_schema = copy.deepcopy(components["schemas"][schema_name])
            return resolve_ref(resolved_schema, components)
            # else:
            #     return schema  # leave unresolved if not under components/schemas
        else:
            return {k: resolve_ref(v, components) for k, v in schema.items()}
    elif isinstance(schema, list):
        return [resolve_ref(item, components) for item in schema]
    else:
        return schema


# all components
def generate_from_components(components: dict):
    """Resolve $ref and generate example JSON for each schema in components."""
    results = {}

    for name, schema in components["schemas"].items():
        resolved_schema = resolve_ref(schema, components)

        try:
            example = JSF(resolved_schema)
        except Exception as e:
            example = f"[Error generating: {e}]"

        results[name] = example.generate()

    return results


def openapi_parse(spec_path: str, base_url: str = ""):
    json_data = read_spec_json(spec_path)

    info = json_data.get("info", {})
    info_template = Template(get_template("info"))
    info_content = info_template.substitute(**info)

    components = json_data.get("components", {})
    securitySchemes = components.get("securitySchemes", {})

    auth_schemes = get_auth_format(securitySchemes)
    auths = Template(get_template("auth")).substitute(auths=auth_schemes.strip())

    paths = OrderedDict(json_data.get("paths", {}))
    combined_path_content = get_path_content(
        paths,
        securitySchemes,
        base_url,
        components,
    )

    content = Template(get_template("combined")).substitute(
        info=info_content.strip(),
        auths=auths.strip(),
        paths=combined_path_content.strip(),
    )

    # write MD beside input file
    output_path = os.path.join(os.path.dirname(spec_path), "openapi.md")
    write_md(content, output_path)

    print(f"✅ Markdown generated at: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: openapi_parser <path-to-openapi.json> <server's base_url>")
        sys.exit(1)

    base_url = ""

    if len(sys.argv) > 2:
        base_url = sys.argv[2]

    spec_path = sys.argv[1]

    if not os.path.exists(spec_path):
        print(f"❌ File not found: {spec_path}")
        sys.exit(1)

    openapi_parse(spec_path, base_url)


if __name__ == "__main__":
    main()
