# ObsidianPy - Python Package for Complex Operations on Obsidian Vault

```
obsidianpy/
├── docs
│   └── overview.md
├── obsidianpy
│   ├── core
│   │   ├── hash_func.py
│   │   ├── __init__.py
│   │   └── interfaces.py
│   ├── graph
│   │   └── __init__.py
│   └── notes
│       ├── contents.py
│       ├── __init__.py
│       └── note.py
├── Readme.md
└── tests
```

## TODO
- Add ruff or other style handling tools.
- Note attributes should be protected or private.
- Define Note Contents interface and class
- Suppose note contents include links, how to construct networkx graph based on those (and hashes).
- Add more todos

## Instalation
Navigate to cloned repo and run:
```
pip install -r requirements.txt
pip install -e .
```
