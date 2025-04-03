from datetime import datetime
from typing import Protocol, Any



# TODO: This is placeholder
class ContentsObject(Protocol):
    
    content: Any

    def get_content(self) -> Any:
        ...
    
    def set_content(self, content: Any) -> None:
        """
        This is a full replacement of the content.
        """
        ...
    
    def __str__(self) -> str:
        ...


class ObsidianObject(Protocol):
    
    title: str
    relative_path: str
    _last_modification_date: datetime
    __hash_val: str  # TODO would we like to integrate it with default python hashing mechanisms?
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


class ObsidianLink(Protocol):

    # TODO This should be removed probably. I will have link abstract class do the heavy lifting.

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


class QueryableObject(Protocol):
    title_to_hash: dict[str, str]

    def get_hash_of(self, title) -> str:
        ...