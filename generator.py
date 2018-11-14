import numpy as np
from process import Process

class Generator:
	def __init__(self):
		pass

	def read_input(self, path='input.txt'):
		file = open(path, 'r')
		lines = file.readlines()
		file.close()
		lines = [i[:-1] if i[-1] == '\n' else i for i in lines]
		num_processes = int(lines[0])
		arrival = [float(i) for i in lines[1].split(' ')]
		burst = [float(i) for i in lines[2].split(' ')]
		priority = float(lines[3])
		return num_processes, arrival, burst, priority


	def generate_processes(self, input_path='input.txt', output_path='output.txt'):
		num_processes, arrival_params, burst_params, priority_params = self.read_input(input_path)
		processes = []
		for i in range(num_processes):
			arrival_time = np.around(np.abs(np.random.normal(arrival_params[0], arrival_params[1])), 1)
			burst_time = np.around(np.abs(np.random.normal(burst_params[0], burst_params[1])), 1)
			priority = np.random.poisson(priority_params)
			processes.append(Process(i+1, arrival_time, burst_time, priority))
		self.out_processes(processes, output_path)
		return processes


	def out_processes(self, processes, path='output.txt'):
		n = len(processes)
		file = open(path, 'w')
		file.write(str(n) + '\n')
		for i in range(n):
			file.write("{} {} {} {}\n".format(processes[i].id, processes[i].arrival, processes[i].burst, processes[i].priority))
		file.close()



if __name__ == "__main__":
	generator = Generator()
	processes = generator.generate_processes()