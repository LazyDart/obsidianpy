# ObsidianPy - Python Package for Complex Operations on Obsidian Vault

**Project is in development stage**
Write to me for feature requests.

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

Decisions:

Links will be abstract class, as they have many different subtypes however all are text-based parts of text based content objects.
Contents is Protocol, as there are contents which are images/documents and contents which are texts (default case).


## TODO
- Must decide whether OBSIDIAN OBJECT should be interface or abstract class.
- Add ruff or other style handling tools.
- Note attributes should be protected or private.
- Define Note Contents interface and class
- Add obsidian link scanning as a Note Contents method.
- Suppose note contents include links, how to construct networkx graph based on those (and hashes).
- Add more todos

## Instalation
Navigate to cloned repo and run:
```
pip install -r requirements.txt
pip install -e .
```
