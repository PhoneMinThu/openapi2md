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
./openapi2md/main.py --distpath ./openapi2md/dist
```

> copy to bin

- `openapi2md`

```bash
cp ./openapi2md/dist/main ~/.local/bin/openapi2md
```

---

## Remove build files

```bash
rm -rf ./build && \
rm -rf **/*dist/ && \
rm -rf **/*main.spec
```

---
