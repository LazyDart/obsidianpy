from datetime import datetime
from typing import Protocol

# TODO: This is placeholder
class ContentsObject(Protocol):
    
    content: str

    


class ObsidianObject(Protocol):
    
    title: str
    relative_path: str
    _last_modification_date: datetime
    __hash_val: str # TODO Isn't it int?
    content: ContentsObject

    @property
    def path(self) -> str:
        ...

    @property
    def abs_path(self) -> str:
        ...
    
    @property
    def extension(self) -> str:
        ...

    def get_hash(self) -> str:
        ...
