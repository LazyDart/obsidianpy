from abc import ABC, abstractmethod

from interfaces import ContentsObject
from link import Link

class TextContents(ABC, ContentsObject):

    content: str
    links: list[Link]
    # TODO things like encoding etc.

    def __init__(self, content: str):
        super().__init__()

        self.content =  content
        self.links = self.extract_links()

    # TODO get_content?


    def insert_content(self, start: int, content: str) -> None:
        """
        This is an insert operation. It more beneficial to use it for link update performance.
        start: string index of where to insert the content.
        content: content to be inserted.
        """
        raise NotImplementedError("insert_content must be implemented in ABC")

    # TODO Can I add a bunch of helper functions that allow text replacement, but will utilize delete/insert operations?
    def delete_content(self, start: int, end: int) -> None:
        """
        This is a delete operation. It more beneficial to use it for link update performance.
        start: string index of where to start the deletion.
        end: string index of where to end the deletion.
        """
        raise NotImplementedError("delete_content must be implemented in ABC")

    @abstractmethod
    def extract_links(self) -> list[Link]:
        """
        This method must be abstract, as non-obsidian type of documents have different criteria for calling someting a link.
        """
        pass

    def _update_links(self, start: int, diff_len: int) -> None:
        """
        This is a helper function to update links after a content change.
        start: string index of where the change starts.
        diff_len: difference in length of the content.
        """
        raise NotImplementedError("_update_links must be implemented in ABC")

    def __str__(self) -> str:
        # TODO Placeholder
        return f"Content({self.content[:100] + '...' if len(self.content) > 100 else ''})"


class BinaryContents(ABC, ContentsObject):
    
    content: bytes

    # TODO