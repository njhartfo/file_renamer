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
		if self.prefixEdit.text():
			self.renameFilesButton.setEnabled(True)
		else:
			self.renameFilesButton.SetEnabled(False)
		
	def loadFiles(self):
		self.dstFileList.clear()
		if self.dirEdit.text():
			intiDir = self.dirEdit.text()
		else:
			initDir = str(Path.home())
		files, filter = QFileDialog.getOpenFileNames(
			self, "Choose Files to Rename", initDir, filter=FILTERS
		)
		if len(files) > 0:
			fileExtension = filter[filter.index("*") : -1]
			self.extensionLabel.setText(fileExtension)
			scrDirName = str(Path(files[0]).parent)
			self.dirEdit.setText(srcDirName)
			for file in files:
				self._files.append(Path(file))
				self.scrFileList.addItem(file)
			self._fileCount = len(self._files)
			self._updateStateWhenFilesLoaded()
		
	def _updateStateWhenFilesLoaded(self):
		self.prefixEdit.setEnabled(True)
		self.prefixEdit.setFocus(True)
	
	def renameFiles(self):
		self._runRenamerThread()
		self._updateStateWhileRenaming()
		
	def _updateStateWhileRenaming(self):
		self.loadFilesButton.setEnabled(False)
		self.renameFilesButton.setEnabled(False)
		
	def _runRenamerThread(self):
		
	def _updateStateWhenFileRenamed(self, newFile):
		self._files.popleft()
		self.scrFileList.takeItem(0)
		self.dstFileList.addItem(str(newFile))
		
	def _updateProgressBar(self, fileNumber):
		progressPercent = int(fileNumber / self._filesCount * 100)
		self.progressBar.setValue(progressPercent)
