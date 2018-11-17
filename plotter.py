import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



class ProcessesPlotter:

	def __init__(self):
		pass

	def getPlottingPoints(self,detailedOutput):
		x=[]
		y=[]
		for p in detailedOutput:
			x.append(p[1])
			y.append(p[0])
			x.append(p[2])
			y.append(p[0])
		return x,y	
	
	#this function takes the start and end time of each process as the x axis
	#and the ids of processes as the y axis
	def plot(self, detailedOutput):
		figure=Figure(figsize=(5, 4), dpi=100)
		#print(detailedOutput)
		x, y = self.getPlottingPoints(detailedOutput)
		new_x = []
		new_y = []
		i = 0
		while i < len(x):
			new_x.append(x[i])
			new_y.append(0)
			new_x.append(x[i])
			new_y.append(y[i])
			i += 1
			new_x.append(x[i])
			new_y.append(y[i])
			new_x.append(x[i])
			new_y.append(0)
			i += 1
		plt.plot(new_x, new_y)
		plt.show()
		figure.add_subplot(111).plot(new_x,new_y)
		return figure