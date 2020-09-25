from .base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'pluginslist'
        self.default_action = 'pluginslist'

    def action_pluginslist(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
            self.vim.command('e ' + str(filepath))
            self.vim.command('pclose')

    def action_preview(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
            self.vim.command('pclose!')
            self.vim.command('vs')
            self.vim.command('setl previewwindow')
            self.vim.command('e ' + str(filepath))
