

class Process:
	def __init__(self, idd, arrival, burst, priority):
		self.id = idd
		self.arrival = arrival
		self.burst = burst
		self.priority = priority
		self.end = 0
		self.remaining_time = burst


	def get_waiting_time(self):
		return self.end - (self.arrival + self.burst)


	def get_turnaround_time(self):
		return self.end - self.arrival


	def get_weighted_turnaround_time(self):
		return self.get_turnaround_time() / self.burst


	def __str__(self):
		return "\nid: {}\narrival time: {}\nburst time: {}\npriority: {}\nend time: {}\nwaiting time: {}\nturnaround time: {}\nweighted turnaround time: {}\n".format(self.id, self.arrival, self.burst, self.priority, self.end, self.get_waiting_time(), self.get_turnaround_time(), self.get_weighted_turnaround_time())
