from .base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'pluginslist'
        self.default_action = 'pluginslist'

    def action_pluginslist(self, context):
        for target in context['targets']:
            filepath = target['word']
            print(filepath)

    def action_preview(self, context):
        filepath = context['targets']
        filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
        print(filepath)
        return True
