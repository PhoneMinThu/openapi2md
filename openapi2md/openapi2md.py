import json
import sys
import os
from string import Template
from collections import OrderedDict


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
    with open(output_path, "w") as api_doc:
        api_doc.write(content)


def get_auth_format(schemes):
    auth_schemes = ""
    for key, scheme in schemes.items():
        auth_schemes += f"**`{key}`** _({scheme.get('type')}, {scheme.get('scheme')})_"
    return auth_schemes


def get_path_content(paths, securitySchemes, base_url=""):
    path_content_json = {}
    for path, path_info in paths.items():
        endpoint = f"{base_url}{path}"
        for method, method_info in path_info.items():
            tags = method_info.get("tags", ["Default"])[0]
            summary = method_info.get("summary", "No summary provided")

            security_schemes = ""
            for security in method_info.get("security", []):
                for key, _ in security.items():
                    scheme = securitySchemes.get(key, {})
                    security_schemes += (
                        f"**`{key}`** _({scheme.get('type')}, {scheme.get('scheme')})_"
                    )
            security_schemes = "- Authorizations: " + (
                security_schemes.strip() if security_schemes else "**`None`**"
            )

            path_template = Template(get_template("path"))
            path_content = path_template.substitute(
                endpoint=endpoint.strip(),
                auths=security_schemes,
                method=method.upper(),
                summary=summary.strip(),
            )
            path_content_json.setdefault(tags, []).append(path_content)

    combined_path_content = ""
    paths_template = Template(get_template("paths"))
    for tags, contents in path_content_json.items():
        paths_content = "".join(contents)
        combined_path_content += paths_template.substitute(
            tags=tags, paths=paths_content.strip()
        )

    return combined_path_content


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
    combined_path_content = get_path_content(paths, securitySchemes, base_url)

    content = Template(get_template("combined")).substitute(
        info=info_content.strip(),
        auths=auths.strip(),
        paths=combined_path_content.strip(),
    )

    # write MD beside input file
    output_path = os.path.join(os.path.dirname(spec_path), "openapi.md")
    write_md(content, output_path)

    print(f"✅ Markdown generated at: {output_path}")
