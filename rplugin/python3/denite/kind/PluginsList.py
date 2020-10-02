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
            self.vim.command('let pluginpath = get(g:, "install_plugin_list", "~/list.toml")')
            installpath = self.vim.eval("pluginpath")
            self.vim.command('e ' + str(installpath))
            self.vim.command('pclose!')
            self.vim.command('goto 1')
            self.vim.command('s /^\[\[plugins\]\]/\r[[plugins]]')
            self.vim.command('goto 1')
            self.action_append(context)
            self.vim.command('s /$/\'')
            self.vim.command('s /^/[[plugins]]\rrepo = \'')
            self.vim.command('nohlsearch')

    # def action_PluginsReadme(self, context):
    def action_preview(self, context):
        self.vim.command('let check_ghvim_for_readme = !empty(globpath(&rtp, "autoload/gh/gh.vim"))')
        ghcheck = self.vim.eval("check_ghvim_for_readme")
        self.vim.command('let use_gh = get(g:, "pluginlist_use_gh", 0)')
        ghuse = self.vim.eval("use_gh")
        for target in context['targets']:
            filepath = target['word']
            self.vim.command('pclose!')
            if ghcheck and ghuse:
                    self.vim.command('new gh://' + str(filepath) + '/readme')
            else:
                    filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../../../../vim-pluginlist/ReadMe/" + str(filepath)))
                    self.vim.command('vs')
                    self.vim.command('setl previewwindow')
                    self.vim.command('vie ' + str(filepath))
