import os
from FileObject import FileObject


class FileListObject:
	path = None
	files = []

	def __init__(self, path):
		self.path = path

		self.files = self.populateList()

	def populateList(self):
		newList = []
		for (root, dirs, files) in os.walk(self.path):
			for currentFileName in files:
				currentFilePath = root + '/' + currentFileName
				myFile = FileObject(currentFilePath)
				newList.append(myFile)

		return newList