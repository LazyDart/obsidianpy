from datetime import datetime
from os import path

from obsidianpy.notes.contents import NoteContent
from obsidianpy.core.interfaces import ObsidianObject
from obsidianpy.core.hash_func import obsidian_note_hash


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
        self.content = NoteContent(content)
        self.__hash_val = obsidian_note_hash(relative_path, modification_date)

    @classmethod
    def from_filepath(cls, file_path: str):
        extension = path.splitext(file_path)[1]
        
        title = path.basename(file_path)[:-(len(extension))]
        
        return Note(
            title=title,
            relative_path=file_path,
            modification_date=datetime.fromtimestamp(path.getmtime(file_path)),
            content=open(file_path, 'r').read()
        )

    def get_hash(self) -> str:
        return self.__hash_val
