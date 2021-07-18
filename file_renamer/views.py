# _*_ coding: utf-8 _*_
# rename/views.py

"""This module provides the Renamer main window."""

from collections import deque
from pathlib import Path

from PyQt5.QtCore import QtThread
from PyQt5.QtWidgets import QFileDialog, QWidget

from .rename import Renamer
from .ui.window import Ui_Window

FILTERS = ";;".join(
	(
		"PNG Files (*.png)",
		"JPEG Files (*.jpeg)",
		"JPG Files (*.jpg)",
		"GIF Files (*.gif)",
		"Text Files (*.txt)",
		"Python Files (*.py)",
	)
)


class Window(QWidget, Ui_Window):
	def __init__(self):
		super().__init__()
		self._files = deque()
		self._filesCount = len(self._files)
		self._setupUI()
		self._connectSignalsSlots()
		
	def _setupUI(self):
		self.setupUi(self)
		self._updateStateWhenNoFiles()
		
	def _updateStateWhenNoFiles(self):
		self._filesCount = len(self._files)
		self.loadFilesButton.setEnabled(True)
		self.loadFilesButton.setFocus(True)
		self.renameFilesButton.setEnabled(False)
		self.prefixEdit.clear()
		self.prefixEdit.setEnabled(False)
		
	def _connectSignalsSlots(self):
		self.loadFilesButton.clicked.connect(self.loadFiles)
		self.renameFilesButton.clicked.connect(self.renameFiles)
		self.prefixEdit.TextChanged.connect(self._updateStateWhenReady)
		
	def _updateStateWhenReady(self):
		
	def loadFiles(self):
		
	def _updateStateWhenFilesLoaded(self):
	
	def renameFiles(self):
		
	def _updateStateWhileRenaming(self):
		
	def _runRenamerThread(self):
		
	def _updateStateWhenFileRenamed(self, newFile):
		
	def _updateProgressBar(self, fileNumber):
