from .api import *   # noqa; F401, F403
from .jni import *   # noqa; F401, F403
from .types import *  # noqa; F401, F403

__version__ = '0.2.4'

_log = JavaClass("org/apache/logging/log4j/LogManager").getLogger("Python")

import io
class _StdoutWrapper(io.StringIO):
    def flush(self):
        for line in self.getvalue().split("\n"):
            if line != "":
                _log.info(line)
                self.truncate(0)
sys.stdout = _StdoutWrapper()

class _StderrWrapper(io.StringIO):
    def flush(self):
        for line in self.getvalue().split("\n"):
            if line != "":
                _log.error(line)
                self.truncate(0)
sys.stderr = _StderrWrapper()