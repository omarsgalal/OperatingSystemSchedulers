from scheduler import Scheduler
from plotter import ProcessesPlotter

class FCFS(Scheduler):
	def __init__(self,contextTime):
		Scheduler.__init__(self)
		self.passed_time = 0
		self.contextTime=contextTime
	def schedule(self):
		outputProccesses=[]
		detailedOutput=[]
		if(len(self.processes)==0):
			return []
		self.processes.sort(key = lambda x: x.arrival)
		
		for i in range( len(self.processes)):
			if (self.processes[i].arrival>self.passed_time):
				self.passed_time=self.processes[i].arrival
			self.processes[i].end=self.processes[i].burst+self.passed_time
			self.processes[i].remaining_time=0
			detailedOutput.append([self.processes[i].id,self.passed_time,self.processes[i].burst+self.passed_time])
			outputProccesses.append(self.processes[i])
			self.passed_time+=self.processes[i].burst+self.contextTime
			'''if i==0:
				self.processes[i].end=self.processes[i].arrival+self.processes[i].burst
				self.processes[i].remaining_time=0
				self.passed_time=self.processes[i].arrival
				detailedOutput.append([self.processes[i].id,self.passed_time,self.processes[i].burst+self.passed_time])

				self.passed_time+=self.processes[i].burst+self.contextTime
				outputProccesses.append(self.processes[i])
				continue
			
			self.processes[i].end=self.passed_time+self.processes[i].burst
			self.processes[i].remaining_time=0
			detailedOutput.append([self.processes[i].id,self.passed_time,self.processes[i].burst+self.passed_time])

			self.passed_time+=self.processes[i].burst+self.contextTime
			outputProccesses.append(self.processes[i])'''
		return outputProccesses,detailedOutput
if __name__ == "__main__":
	x=[]
	y=[]
	fcfs = FCFS(3)
	fcfs.read_processes()
	processes,detailedOutput = fcfs.schedule()
	outfile = open('scheduled_processes.txt', 'w')
	for p in processes:
		outfile.write(str(p))
	outfile.close()
	for p in detailedOutput:
		print(p)
		x.append(p[1])
		x.append(p[2])
		y.append(p[0])
		y.append(p[0])	
	plotter = ProcessesPlotter()
	plotter.plot(x, y)	