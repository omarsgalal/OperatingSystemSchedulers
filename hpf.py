from scheduler import Scheduler
from plotter import ProcessesPlotter

class HPF(Scheduler):
	def __init__(self, context_switch):
		Scheduler.__init__(self)
		self.passed_time = 0
		self.current_processes = []
		self.context_switch = context_switch

	def get_max_priority(self):
		return max(self.processes, key=lambda x:x.priority).priority

	def schedule(self):
		num_processes = len(self.processes)
		if num_processes == 0:
			return []

		final_processes = []
		detailedOutput=[]

		self.processes.sort(key = lambda x: x.arrival)

		max_priority = self.get_max_priority()

		i = 0

		self.passed_time += self.processes[i].arrival

		while i < num_processes or len(self.current_processes) > 0:

			while i < num_processes and self.processes[i].arrival <= self.passed_time:
				self.current_processes.append(self.processes[i])
				self.current_processes[-1].priority = max_priority - self.current_processes[-1].priority
				i += 1

			self.current_processes.sort(key = lambda x: x.id)
			self.current_processes.sort(key = lambda x: x.priority)


			detailedOutput.append([self.current_processes[0].id,self.passed_time,self.current_processes[0].burst+self.passed_time])
			self.passed_time += self.current_processes[0].burst + self.context_switch
			self.current_processes[0].end = self.passed_time - self.context_switch
			final_processes.append(self.current_processes[0])
			final_processes[-1].priority = max_priority - final_processes[-1].priority
			self.current_processes = self.current_processes[1:]


			if len(self.current_processes) == 0 and i < num_processes and self.passed_time < self.processes[i].arrival:
				self.passed_time = self.processes[i].arrival



		return final_processes,detailedOutput


if __name__ == "__main__":
	hpf = HPF(1)
	hpf.read_processes()
	processes = hpf.schedule()
	outfile = open('scheduled_processes.txt', 'w')
	x = []
	y = []
	for p in processes:
		outfile.write(str(p))
		x.append(p.end - p.burst)
		y.append(p.id)
		x.append(p.end)
		y.append(p.id)
	plotter = ProcessesPlotter()
	plotter.plot(x, y)
	outfile.close()