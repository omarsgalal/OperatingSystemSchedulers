from scheduler import Scheduler


class HPF(Scheduler):
	def __init__(self):
		Scheduler.__init__(self)
		self.passed_time = 0
		self.current_processes = []

	def get_max_priority(self):
		return max(self.processes, key=lambda x:x.priority).priority

	def schedule(self):
		num_processes = len(self.processes)
		if num_processes == 0:
			return []

		final_processes = []

		self.processes.sort(key = lambda x: x.arrival)

		max_priority = self.get_max_priority()

		self.current_processes.append(self.processes[0])
		self.current_processes[0].priority = max_priority - self.current_processes[0].priority

		i = 1
		while i < num_processes and self.processes[i].arrival == self.processes[i-1].arrival:
			self.current_processes.append(self.processes[i])
			self.current_processes[-1].priority = max_priority - self.current_processes[-1].priority
			i += 1

		self.passed_time += self.current_processes[0].arrival

		while len(self.current_processes) > 0:

			self.current_processes.sort(key = lambda x: x.id)
			self.current_processes.sort(key = lambda x: x.priority)

			self.passed_time += self.current_processes[0].burst
			self.current_processes[0].end = self.passed_time
			final_processes.append(self.current_processes[0])
			final_processes[-1].priority = max_priority - final_processes[-1].priority
			self.current_processes = self.current_processes[1:]

			if len(self.current_processes) == 0 and i < num_processes:
				self.passed_time = self.processes[i].arrival

			while i < num_processes and self.processes[i].arrival <= self.passed_time:
				self.current_processes.append(self.processes[i])
				self.current_processes[-1].priority = max_priority - self.current_processes[-1].priority
				i += 1



		return final_processes


if __name__ == "__main__":
	hpf = HPF()
	hpf.read_processes()
	processes = hpf.schedule()
	outfile = open('scheduled_processes.txt', 'w')
	for p in processes:
		outfile.write(str(p))
	outfile.close()