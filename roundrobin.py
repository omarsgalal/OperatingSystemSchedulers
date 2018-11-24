from scheduler import Scheduler
from plotter import ProcessesPlotter

class CircularQueue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		item = self.queue[0]
		self.queue = self.queue[1:]
		return item

	def rotate(self):
		item = self.queue[0]
		self.queue[:-1] = self.queue[1:]
		self.queue[-1] = item


	def __getitem__(self, key):
		return self.queue[key]


	def front(self):
		if len(self.queue) > 0 :
			return self.queue[0]
		else:
			return None


	def back(self):
		return self.queue[-1]


	def __len__(self):
		return len(self.queue)


class RoundRobin(Scheduler):
	def __init__(self, quantum, context_switching):
		Scheduler.__init__(self)
		self.passed_time = 0
		self.current_processes = CircularQueue()
		self.quantum = quantum
		self.context_switching = context_switching


	def schedule(self):
		if self.quantum == 0:
			return
			
		num_processes = len(self.processes)
		if num_processes == 0 or self.quantum == 0:
			return [], []

		final_processes = []
		detailed_processing = []

		self.processes.sort(key = lambda x: x.arrival)

		i = 0

		self.passed_time = self.processes[0].arrival

		while i < num_processes or len(self.current_processes) > 0:

			while i < num_processes and self.processes[i].arrival <= self.passed_time:
				self.current_processes.enqueue(self.processes[i])
				i += 1

			time_taken = min(self.current_processes.front().remaining_time, self.quantum)
			detailed_processing.append([self.current_processes.front().id, self.passed_time, self.passed_time+time_taken])
			self.passed_time += time_taken
			self.current_processes.queue[0].remaining_time -= time_taken
			

			while i < num_processes and self.processes[i].arrival <= self.passed_time:
				self.current_processes.enqueue(self.processes[i])
				i += 1


			if self.current_processes.front().remaining_time > 0:
				self.current_processes.rotate()
			else:
				process = self.current_processes.dequeue()
				process.end = self.passed_time
				final_processes.append(process)

			self.passed_time += self.context_switching


			if len(self.current_processes) == 0 and i < num_processes and self.passed_time < self.processes[i].arrival:
				self.passed_time = self.processes[i].arrival
				#self.passed_time -= self.context_switching

		return final_processes, detailed_processing



if __name__ == "__main__":
	roundrobin = RoundRobin(2.2, 0.8)
	roundrobin.read_processes('processes.txt')
	processes, details = roundrobin.schedule()
	outfile = open('a.txt', 'w')
	for p in processes:
		outfile.write(str(p))
	outfile.close()
	outfile = open('details.txt', 'w')
	x = []
	y = []
	for p in details:
		outfile.write("\nid: {}\nstart time: {}\nend time: {}\n".format(p[0], p[2] - p[1], p[2]))
		x.append(p[2] - p[1])
		y.append(p[0])
		x.append(p[2])
		y.append(p[0])
	outfile.close()
	plotter = ProcessesPlotter()
	plotter.plot(x, y)
