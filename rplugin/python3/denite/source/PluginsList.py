from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'PluginsList'
        self.kind = 'directory'

    def gather_candidates(self, context):
        cmd = ['cat', '~/vim-pluginlist/list']
        candidates = []
        for path in subprocess.run(cmd, check=True, universal_newlines=True, stdout=subprocess.PIPE).stdout.split()
            print(aa)
            candidates += [{'word': "{0} {1}".format(path, "test"),'action__text': path}]
        return candidates
