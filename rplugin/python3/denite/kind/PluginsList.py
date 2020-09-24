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
            filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
            self.vim.command('e ' + str(filepath))
            self.vim.command('e ' + str(filepath))

    def action_preview(self, context):
        filepath = context['targets'][0]['word']
        filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
        print("aaaa")
        return True
