from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'PluginsList'
        self.kind = 'pluginslist'

    def gather_candidates(self, context):
        cmd = ['cat', '~/vim-pluginlist/list']
        candidates = []
        return [{'word': path}
        for path in subprocess.run(cmd,
                check=True,
                universal_newlines=True,
                stdout=subprocess.PIPE
                ).stdout.split()]
