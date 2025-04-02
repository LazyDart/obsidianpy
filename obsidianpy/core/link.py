from abc import ABC, abstractmethod

from interfaces import QueryableObject

class Link(ABC):
    
    def __init__(self, text: str, hash_container: QueryableObject):
        super().__init__()
        self.text = text
        self.target_note_hash = self._get_target_note_hash(text, hash_container)

    @abstractmethod
    def _get_target_note_hash(
            self,
            text: str, 
            hash_container: QueryableObject
    ) -> str:
        ...