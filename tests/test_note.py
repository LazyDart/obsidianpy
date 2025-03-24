import pytest

from obsidianpy.notes.note import Note
from datetime import datetime

print(Note.from_filepath("tests/test_data/notes/short_note.md").get_hash())

def test_note_from_path():
    note = Note.from_filepath("tests/test_data/notes/short_note.md")
    assert note.title == "short_note"
    assert note.relative_path == "tests/test_data/notes/short_note.md"
    assert note._last_modification_date == datetime(2025, 3, 24, 17, 56, 42, 327090)
    assert note.content.content == "Note written with markdown.\n\n# Lol"
    assert note.get_hash() == "83fbf7508e742501fbfb2baf29dc092f1ef8ac8fd989b1b7cc44a303e384c575"