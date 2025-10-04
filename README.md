## Environment

> [!info] uv as package manager

```bash
uv venv .venv
source ./venv/bin/activate
uv sync
```

---

## Build binary

> [!info] Build binary with pyinstaller

```bash
uv run pyinstaller --onefile \
--add-data "openapi2md/templates:openapi2md/templates" \
main.py
```

> copy to bin

```bash
cp ./dist/main ~/.local/bin/openapi2md
```

---
