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
            installpath = self.vim.command('get(g:, \'install_plugin_list\', \'~/list.toml\')')
            self.vim.command('e ' + str(installpath))
            self.vim.command('pclose!')
            self.vim.command('goto 1')
            self.vim.command('s /^\[\[plugins\]\]/\r[[plugins]]')
            self.action_append(context)
            self.vim.command('s /$/\'')
            self.vim.command('s /^/\r[[plugins]]\rrepo = \'')
            self.vim.command('nohlsearch')

    def action_preview(self, context):
        for target in context['targets']:
            filepath = target['word']
            filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../../../../vim-pluginlist/ReadMe/" + str(filepath)))
            self.vim.command('pclose!')
            self.vim.command('vs')
            self.vim.command('setl previewwindow')
            self.vim.command('e ' + str(filepath))
