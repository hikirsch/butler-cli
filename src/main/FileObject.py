import hashlib


class FileObject:
	path = None
	md5 = None

	def __init__(self, filePath):
		self.path = filePath
		self.createMD5()

	def createMD5(self):
		currentFile = open(self.path, 'r')
		fileContents = currentFile.read()
		self.md5 = hashlib.md5(fileContents).hexdigest()
		currentFile.close()