import os
import sys

from openapi2md.openapi2md import openapi_parse


def main():
    if len(sys.argv) < 2:
        print("Usage: openapi_parser <path-to-openapi.json>")
        sys.exit(1)

    spec_path = sys.argv[1]

    if not os.path.exists(spec_path):
        print(f"❌ File not found: {spec_path}")
        sys.exit(1)

    openapi_parse(spec_path)


if __name__ == "__main__":
    main()

