import hashlib
import os


class FileObject:
	filePath = None
	fileHash = None
	realPath = None

	def __init__(self, filePath):
		self.filePath = filePath
		self.createMD5()
		self.setRealPath()

	def createMD5(self):
		currentFile = open(self.filePath, 'r')
		fileContents = currentFile.read()
		self.fileHash = hashlib.md5(fileContents).hexdigest()
		currentFile.close()

	def setRealPath(self):
		self.realPath = os.path.realpath(self.filePath)