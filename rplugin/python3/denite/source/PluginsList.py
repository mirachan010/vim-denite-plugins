from .base import Base
import subprocess


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'PluginsList'
        self.kind = 'text'

    def gather_candidates(self, context):
        cmd = ['cat', '~/vim-pluginlist/list']
        candidates = []
        return [{'word': path, 'action__path': path}
        for path in subprocess.run(cmd,
                check=True,
                universal_newlines=True,
                stdout=subprocess.PIPE
                ).stdout.split()]
            # candidates += [{'word': "{0} {1}".format(path, "test"),'action__text': path}]
        # return candidates
