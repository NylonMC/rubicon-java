from . import JavaClass
import io
import sys

_log = JavaClass("org/apache/logging/log4j/LogManager").getLogger("Python")

class _StdoutWrapper(io.StringIO):
    def flush(self):
        for line in self.getvalue().split("\n"):
            if line != "":
                _log.info(line)
                # self.truncate(0)
sys.stdout = _StdoutWrapper()

class _StderrWrapper(io.StringIO):
    def flush(self):
        for line in self.getvalue().split("\n"):
            if line != "":
                _log.error(line)
                # self.truncate(0)
sys.stderr = _StderrWrapper()