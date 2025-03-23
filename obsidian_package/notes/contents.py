from obsidian_package.core.interfaces import ContentsObject

# TODO Obviosuly
class NoteContent(ContentsObject):
    def __init__(self, content: str):
        self.content = content