from numpy import round

class Output(object):
	"""docstring for Output"""
	def __init__(self, outputFileName,processes):
		
		self.outputFileName = outputFileName
		self.processes=processes


	def writeOutput(self):
		outfile = open(self.outputFileName, 'w')
		avg_turnaround = 0
		avg_weighted_turaround = 0
		for p in self.processes:
			outfile.write(str(p))
			avg_turnaround += p.get_turnaround_time()
			avg_weighted_turaround += p.get_weighted_turnaround_time()

		avg_turnaround /= len(self.processes)
		avg_weighted_turaround /= len(self.processes)

		avg_turnaround = round(avg_turnaround, 2)
		avg_weighted_turaround = round(avg_weighted_turaround, 2)

		outfile.write("\n\nAverage Turnaround Time = {}\n".format(avg_turnaround))
		outfile.write("Average Weighted Turnaround Time = {}\n".format(avg_weighted_turaround))

		outfile.close()	

		