from .base import Base
import os

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'pluginslist'
        self.default_action = 'pluginslist'

    def action_pluginslist(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = "~/vim-pluginlist/ReadMe/" + str(filepath)
            self.vim.command('e ~/list.toml')
            self.vim.command('pclose')
             _paste(self.vim,target.get('action__text', target['word']), 'p', 'v')

    def action_preview(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../../../vim-pluginlist/ReadMe/" + str(filepath)))
            self.vim.command('pclose!')
            self.vim.command('vs')
            self.vim.command('setl previewwindow')
            self.vim.command('e ' + str(filepath))
