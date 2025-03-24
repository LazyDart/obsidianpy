from obsidian_package.core.interfaces import ObsidianObject
from obsidian_package.core.hash_func import obsidian_note_hash
from datetime import datetime


class Note(ObsidianObject):
    def __init__(
            self, 
            title: str, 
            relative_path: str, 
            modification_date: datetime, 
            content: str
        ):

        self.title = title
        self.relative_path = relative_path
        self._last_modification_date = modification_date
        self.content = content
        self.__hash_val