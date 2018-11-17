class Output(object):
	"""docstring for Output"""
	def __init__(self, outputFileName,processes):
		
		self.outputFileName = outputFileName
		self.processes=processes
	def writeOutput(self):
		outfile = open(self.outputFileName, 'w')
		
		for p in self.processes:
			outfile.write(str(p))

		outfile.close()	

		