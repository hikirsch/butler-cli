import shutil
import os
from FileListObject import FileListObject


class CopyController:
	# Set up variables to None initially
	source = None
	target = None
	sourceList = None
	targetList = None

	def __init__(self, source, target):
		self.source = source
		if self.source[:1] != '/':
			self.source = os.getcwd() + '/' + source

		self.target = target
		if self.target[:1] != '/':
			self.target = os.getcwd() + '/' + target

		self.sourceList = FileListObject(self.source)
		self.targetList = FileListObject(self.target)

	def copy(self, clean):

		if clean:
			if os.path.isdir(self.target):
				shutil.rmtree(self.target)

		if os.path.isdir(self.source):
			if not clean:
				shutil.copy(self.source, self.target)
			else:
				shutil.copytree(self.source, self.target)
				print "Target has been copied.  Thank you."
		else:
			print "Source is not a directory"

		#class CopyController
			# sourceList = CreateList("src")
			# targetList = CreateList("target")

		# walk source & target and compare them
		# CompareLists(sourceList, targetList)

		#class CreateList(basePath) implements FileObject
			# Walk the basePath
			# calls FileObject

#class CompareLists(sourceList, targetList)


x = CopyController("TestData/src", "TestData/target")
print "Done"

# import pyrsync
# unpatched = open("unpatched.file", "rb")
# hashes = pyrsync.blockchecksums(unpatched)