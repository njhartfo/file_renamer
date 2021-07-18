import time
from pathlib import Path
from PyQt5.QtCore import QObject, pyqtSignal


class Renamer(QObject):
  progressed = pyqtSignal(int)
  renamedFile = pyqtSignal(Path)
  finished = pyqtSignal() # come back to review, not sure if correct
  
  def __init__(self, files, prefix):
    super().__init__()
    self._files = files
    self._prefix = prefix
  
  def renameFiles(self):
    # parse through files
    # join under parent file
    # rename
    # emit
