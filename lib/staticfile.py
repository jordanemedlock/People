from definitions import STATIC_DIR
import os

class StaticFile(object):
    def __init__(self, local_dir):
        self.local_dir = local_dir # linchpin

    @property
    def web_dir(self):
        return os.path.join('/static/', self.local_dir)

    @property
    def global_dir(self):
        return os.path.join(STATIC_DIR, self.local_dir)

    def __str__(self):
        return self.web_dir

    def __repr__(self):
        return 'StaticFile('+repr(self.local_dir)+')'