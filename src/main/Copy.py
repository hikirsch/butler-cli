# copy target to destination
import hashlib
import shutil
import os


class CopyController:
	# Set up variables to None initially
	source = None
	target = None

	def __init__(self):
		# Not sure what we need here yet
		print "Initialized"

	def copy(self, source, target, clean):

		if clean:
			if os.path.isdir(target):
				shutil.rmtree(target)

		if os.path.isdir(source):
			if not clean:
				sourceHash = CopyController.md5creator(source)
				targetHash = CopyController.md5creator(target)
				print sourceHash
				print targetHash

				shutil.copy(source, target)
			else:
				shutil.copytree(source, target)
				print "Target has been copied.  Thank you."
		else:
			print "Source is not a directory"

	def md5creator(self, myFile):
		return hashlib.md5(myFile)

	def listAll(self, source):
		newArray = []

		myDirectory = os.path.realpath(source)

		for root, dirs, files in os.walk(myDirectory):
			for name in files:
				newArray.append(os.path.join(root, name))
			for name in dirs:
				newArray.append(os.path.join(root, name))

		return newArray

		# for files in source:
		#     pass


# x = CopyController()

# clean = False

# x.copy("src", "target", clean)
# listOfFiles = x.listAll("src")
# listOfSourceHash = []
# listOfTargetHash = []
#
# for myFile in listOfFiles:
# 	print myFile
# 	currentFile = open(myFile, 'r')
# 	print (hashlib.md5(currentFile.read()).hexdigest())