import sys

from PyQt5.QtWidgets import QApplication
from .views import Window


def main():
  # Create the applicaiton
  app = QApplication(sys.argv)
  # Create main window
  win = Window()
  win.show()
  sys.exit(app.exec())
