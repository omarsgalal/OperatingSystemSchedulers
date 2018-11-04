import matplotlib.pyplot as plt


class ProcessesPlotter:
	def __init__(self):
		pass

	#this function takes the start and end time of each process as the x axis
	#and the ids of processes as the y axis
	def plot(self, x, y):
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