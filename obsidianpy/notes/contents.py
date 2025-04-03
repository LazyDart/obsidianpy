from obsidianpy.core.contents_abc import TextContents

# TODO Obviosuly
class NoteContents(TextContents):
    
    def __init__(self, content:str):
        super().__init__(content)

    def extract_links(self):
        raise NotImplementedError("NoteContents should have their own way of finding links.")