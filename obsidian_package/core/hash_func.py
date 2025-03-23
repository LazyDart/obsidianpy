from datetime import datetime
from hashlib import sha256

# TODO might be needed to include information about the time zone.
# TODO must be decided whether to be case sensitive or not.

def obsidian_note_hash(relative_path: str, modification_date: datetime) -> str:
    return sha256(f"{relative_path}{modification_date}".encode()).hexdigest()