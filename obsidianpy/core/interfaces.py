from datetime import datetime
from typing import Protocol


class ObsidianLink(Protocol):

    # TODO: This is a placeholder. 
    # TODO: It might be cool to keep location information in the link object. Or maybe it will slow things down?

    source: str
    target: str
    context: str

    def get_source(self) -> str:
        ...
    
    def get_target(self) -> str:
        ...
    
    def get_context(self) -> str:
        ...
    
    def set_source(self, source: str) -> None:
        ...
    
    def set_target(self, target: str) -> None:
        ...
    
    def set_context(self, context: str) -> None:
        ...
    
    def __str__(self) -> str:
        ...


# TODO: This is placeholder
class ContentsObject(Protocol):
    
    content: str
    links: list[str] 

    def get_content(self) -> str:
        ...
    
    def set_content(self, content: str) -> None:
        """
        This is a full replacement of the content.
        """
        ...

    def insert_content(self, start: int, content: str) -> None:
        """
        This is an insert operation. It more beneficial to use it for link update performance.
        start: string index of where to insert the content.
        content: content to be inserted.
        """
        ...

    # TODO Can I add a bunch of helper functions that allow text replacement, but will utilize delete/insert operations?
    def delete_content(self, start: int, end: int) -> None:
        """
        This is a delete operation. It more beneficial to use it for link update performance.
        start: string index of where to start the deletion.
        end: string index of where to end the deletion.
        """
        ...

    def extract_links(self) -> list[str]:
        ...

    def update_links(self, start: int, diff_len: int) -> None:
        """
        This is a helper function to update links after a content change.
        start: string index of where the change starts.
        diff_len: difference in length of the content.
        """
        ...
    
    def __str__(self) -> str:
        ...


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

    def __str__(self) -> str:
        ...