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
            self.action_append(context)
            self.vim.command('s /$/\'')
            self.vim.command('s /^/[[plugin]]\r')
            self.vim.command('nohlsearch')

    def action_preview(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../../../vim-pluginlist/ReadMe/" + str(filepath)))
            self.vim.command('pclose!')
            self.vim.command('vs')
            self.vim.command('setl previewwindow')
            self.vim.command('e ' + str(filepath))
