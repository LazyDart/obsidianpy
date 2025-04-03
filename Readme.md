# ObsidianPy - Python Package for Complex Operations on Obsidian Vault

**Project is in development stage**
Write to me for feature requests.

```
obsidianpy/
├── docs
│   └── overview.md
├── .gitignore
├── obsidianpy
│   ├── core
│   │   ├── contents_abc.py
│   │   ├── hash_func.py
│   │   ├── __init__.py
│   │   ├── interfaces.py
│   │   └── link.py
│   ├── graph
│   │   └── __init__.py
│   ├── __init__.py
│   └── notes
│       ├── contents.py
│       ├── __init__.py
│       └── note.py
├── pyproject.toml
├── Readme.md
├── requirements.txt
└── tests
    ├── test_data
    │   └── notes
    │       ├── long_note.md
    │       └── short_note.md
    └── test_note.py
```

Decisions:

Links will be abstract class, as they have many different subtypes however all are text-based parts of text based content objects.
Contents is Protocol, as there are contents which are images/documents and contents which are texts (default case).


## TODO

### Important
- Define TextContents ABC methods (not abstract, I think).
- Define Note Contents extract links method.
- Finish Definition of Note Contents class
- Multiple links linking to the same file might be possible. Should we store them separately or not?
    - It's either separate links that must be updated individually 
    - or a one link with multiple positions.
- Note attributes should be protected or private.
- Add obsidian link scanning as a Note Contents method.
- Suppose note contents include links, how to construct networkx graph based on those (and hashes).

### Less Important
- Add ruff or other style handling tools.
- Implement binary contents abstract class and their children.
- encodings must be considered at some points

## Instalation
Navigate to cloned repo and run:
```
pip install -r requirements.txt
pip install -e .
```
