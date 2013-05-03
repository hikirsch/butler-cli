import unittest
# from src.main.FileObject import FileObject


class myTest(unittest.TestCase):
	def test(self):
		self.assertEqual(1,1,"test")
		# myFile = FileObject("TestData/src/source.txt")

	def testName(self):
		self.assertEqual(1,1,"testName")

	def nameTest(self):
		self.assertEqual(1,1,"nameTest")

	def anotherTestTestingWithoutIt(self):
		self.assertEqual(1,1,"anotherTestTestingWithoutIt")