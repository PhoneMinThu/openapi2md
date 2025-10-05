## Environment

> [!info] uv as package manager

```bash
uv venv .venv
source ./venv/bin/activate
uv sync
```

---

## Run

```bash
python3 ./openapi2md/main.py openapi.json localhost:8000 target/openapi.md
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
sudo rm -rf ./build/ && \
sudo rm -rf **/*dist/ && \
sudo rm -rf ./py_openapi.egg-info/ && \
sudo rm -rf **/*main.spec
```

---

## uv build and publish

- build

```bash
uv build
```

- publish

```bash
uv publish
```

- uvx run

```bash
uvx py-openapi2md
```

---
