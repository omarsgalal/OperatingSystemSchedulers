from process import Process


class Scheduler:
	def __init__(self):
		self.processes = []

	def read_processes(self, path="output.txt"):
		file = open(path, 'r')
		lines = file.readlines()
		file.close()
		lines = [i[:-1] if i[-1] == '\n' else i for i in lines]
		num_processes = int(lines[0])
		for i in range(num_processes):
			params = lines[i+1].split(' ')
			idd = int(params[0])
			arrival = float(params[1])
			burst = float(params[2])
			proirity = int(params[3])
			self.processes.append(Process(idd, arrival, burst, proirity))

	def schedule(self):
		pass