from scheduler import Scheduler


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
		return self.queue[0]


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
		num_processes = len(self.processes)
		if num_processes == 0:
			return []

		final_processes = []
		detailed_processing = []

		self.processes.sort(key = lambda x: x.arrival)

		self.current_processes.enqueue(self.processes[0])

		i = 1
		while i < num_processes and self.processes[i].arrival == self.processes[i-1].arrival:
			self.current_processes.enqueue(self.processes[i])
			i += 1

		self.passed_time += self.current_processes.front().arrival

		while len(self.current_processes) > 0:

			time_taken = min(self.current_processes.front().remaining_time, self.quantum)
			self.passed_time += time_taken
			self.current_processes.queue[0].remaining_time -= time_taken
			detailed_processing.append([self.current_processes.front().id, time_taken, self.passed_time])

			if len(self.current_processes) == 0 and i < num_processes:
				self.passed_time = self.processes[i].arrival
				self.passed_time -= self.context_switching

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

		return final_processes, detailed_processing



if __name__ == "__main__":
	roundrobin = RoundRobin(3, 0.5)
	roundrobin.read_processes()
	processes, details = roundrobin.schedule()
	outfile = open('scheduled_processes.txt', 'w')
	for p in processes:
		outfile.write(str(p))
	outfile.close()
	outfile = open('details.txt', 'w')
	for p in details:
		outfile.write("\nid: {}\nstart time: {}\nend time: {}\n".format(p[0], p[2] - p[1], p[2]))
	outfile.close()

