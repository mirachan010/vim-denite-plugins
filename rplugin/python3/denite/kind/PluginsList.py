from .base import Base
import os.path

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'pluginslist'
        self.default_action = 'pluginslist'

    def action_pluginslist(self, context):
        for target in context['targets']:
            filepath = target['word']
            self.vim.command('let pluginpath = get(g:, "install_plugin_list", "~/list.toml")')
            installpath = str(self.vim.eval("pluginpath"))
            installpath = os.path.expanduser(installpath)
            installfile = open(installpath, 'a', encoding="utf-8")
            installfile.write("[[plugins]]\n")
            installfile.write("repo = '"+filepath + "'")
            installfile.close()
            self.vim.command('echo '+installpath)

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
