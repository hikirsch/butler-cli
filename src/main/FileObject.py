# import pyrsync
# from pyrsync.pyrsync import blockchecksums
# from pyrsync import pyrsync.pyrsync
from pyrsync import pyrsync


class FileObject:
	path = None
	sha256 = None

	def __init__(self, filePath):
		self.path = filePath
		self.createMD5()

	def createMD5(self):
		currentFile = open(self.path, 'r')

		self.sha256 = pyrsync.blockchecksums(currentFile)

		currentFile.close()