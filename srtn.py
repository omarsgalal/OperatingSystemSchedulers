from scheduler import Scheduler
from plotter import ProcessesPlotter



class SRTN(Scheduler):
	def __init__(self,contextSwitching):
		Scheduler.__init__(self)
		self.passed_time = -1*contextSwitching
		self.contextSwitching=contextSwitching

	def schedule(self):
		
		outputProcesses=[]
		detailedOutput=[]
		currentProcesses=[]
		
		numProcessesLeft=len(self.processes)
		numProcesses=len(self.processes)

		self.processes.sort(key = lambda x: x.arrival)

		self.passed_time = self.processes[0].arrival

		previous_id = -1
		i=0
		if(numProcesses==0):
			return [],[]
		while(numProcessesLeft>0):
			#add elements that recently arrived in the list
			while(i<numProcesses and self.processes[i].arrival<=self.passed_time):
				currentProcesses.append(self.processes[i])
				#print(i)
				i+=1

			if len(currentProcesses)==0:
				self.passed_time = self.processes[i].arrival
				continue
			

			currentProcesses.sort(key = lambda x:x.remaining_time)
			if i==numProcesses:
				currentStep=currentProcesses[0].remaining_time
			else:	
				currentStep=min(currentProcesses[0].remaining_time, self.processes[i].arrival - self.passed_time)
			currentProcesses[0].remaining_time -= currentStep
			detailedOutput.append([currentProcesses[0].id,self.passed_time,currentStep])
			self.passed_time += currentStep

			if   previous_id != currentProcesses[0].id:
				self.passed_time += self.contextSwitching
				previous_id = currentProcesses[0].id
			
			if(currentProcesses[0].remaining_time==0):
				currentProcesses[0].end = self.passed_time
				outputProcesses.append(currentProcesses[0])
				del currentProcesses[0]
				numProcessesLeft-=1
				#print(numProcessesLeft)

			
		return detailedOutput,outputProcesses	

if __name__ == "__main__":
	srtn = SRTN(0)
	srtn.read_processes()
	detailedOutput,processes = srtn.schedule()
	outfile = open('scheduled_processes.txt', 'w')
	for p in processes:
		#print(p)
		outfile.write(str(p))
	outfile.close()
	x=[]
	y=[]
	for p in detailedOutput:
		x.append(p[1])
		y.append(p[0])
		x.append(p[1]+p[2])
		y.append(p[0])

	plotter = ProcessesPlotter()
	plotter.plot(x,y)