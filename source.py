import tkinter as tk
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, simpledialog,OptionMenu,Frame,messagebox
from functools import partial
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from plotter import ProcessesPlotter
from srtn import SRTN
from fcfs import FCFS
from hpf import HPF
from roundrobin import RoundRobin
from output import Output
import matplotlib.pyplot as plt
from generatorDialog import GeneratorDialog
import os



selectedAlgorithm="HPF"


def runAlgorithm(inputFileName,outputFileName,quantumTimeEntry,contextSwitchingTimeEntry):
		
		

		global figurePlotter
		'''if(not(contextSwitchingTimeEntry.isdigit()) or contextSwitchingTimeEntry==""):
			messagebox.showinfo("Error","Please Enter a positive context switching time ")
			return'''
		try:
			contextSwitchTime = float(contextSwitchingTimeEntry)
			if (contextSwitchTime < 0):
				messagebox.showinfo("Error","Please Enter a positive context switch Time ")
				return
		except ValueError:
			messagebox.showinfo("Error","Please Enter a valid positive context switch Time ")
			return

		if(inputFileName=="" or outputFileName==""): 
			return

		if selectedAlgorithm == "RR":
			try:
				quantumTime = float(quantumTimeEntry)
				if quantumTime < 0:
					messagebox.showinfo("Error","Please Enter a positive quantum")
					return
			except ValueError:
				messagebox.showinfo("Error","Please Enter a valid positive quantum")
				return

		exists = os.path.isfile(inputFileName)
 		

		if not(exists):
			messagebox.showinfo("Error","Input file doesn't exist")
			return	

		if selectedAlgorithm == "HPF":
			sched = HPF(contextSwitchTime)
		elif selectedAlgorithm == "FCFS":
			sched = FCFS(contextSwitchTime)
		elif selectedAlgorithm == "RR":
			sched = RoundRobin(quantumTime, contextSwitchTime)
		elif selectedAlgorithm == "SRTN":
			sched = SRTN(contextSwitchTime)


		sched.read_processes(inputFileName)
		outputProcesses, detailedOutput = sched.schedule()
		
		'''if(selectedAlgorithm=="HPF"):
			hpf=HPF(contextSwitchTime,inputFileName)
			outputProcesses,detailedOutput=hpf.schedule()


		if(selectedAlgorithm=="FCFS"):
			fcfs=FCFS(contextSwitchTime)
			fcfs.read_processes(inputFileName)
			outputProcesses,detailedOutput=fcfs.schedule()
			print("FCFS")

		if(selectedAlgorithm=="SRTN"):
			srtn=SRTN(contextSwitchTime,inputFileName)
			outputProcesses,detailedOutput=srtn.schedule()
			print("SRTN")

		if(selectedAlgorithm=="RR"):
			quantumTime=int(quantumTimeEntry) 
			roundrobin=RoundRobin(quantumTime,contextSwitchTime,inputFileName)
			outputProcesses,detailedOutput=roundrobin.schedule()
			print("RR")   '''

		#print (detailedOutput)
		output2FileWriter=Output(outputFileName,outputProcesses)
		output2FileWriter.writeOutput()
		plotter = ProcessesPlotter()
		plt.clf()
		figurePlotter=plotter.plot(detailedOutput)
		#print(figurePlotter)
		#canvas.clear()
		#canvas = FigureCanvasTkAgg(figurePlotter, master=rowFourFrame)  # A tk.DrawingArea.
		#canvas.draw()
		#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
		#canvas.get_tk_widget().update()

def generateProcessess(root):
	d=GeneratorDialog(root)
	root.wait_window(d.top)




def updateParams(quantumTimeEntry,value) :
	
	global selectedAlgorithm
	selectedAlgorithm=value
	
	if(value!="RR"):
		quantumTimeEntry.config(state="disabled")
	else:
		quantumTimeEntry.config(state="normal")



root = tk.Tk()
plotter=ProcessesPlotter()
#global figurePlotter
#figurePlotter=plotter.plot([[1,2,3]])
figurePlotter = None



rowOneFrame = Frame(root)
rowOneFrame.pack()
		
rowTwoFrame = Frame(root)
rowTwoFrame.pack()

rowThreeFrame=Frame(root)
rowThreeFrame.pack()

		
rowFourFrame = Frame(root)
rowFourFrame.pack()


		
outputFileNameLabel=Label(rowTwoFrame,text="Output: ")
outputFileNameLabel.pack(side="left")

outputFileNameEntry=Entry(rowTwoFrame)
outputFileNameEntry.pack(side="left",padx=(0,180))

quantumLabel = Label(rowTwoFrame, text="Quantum Time: ")
quantumLabel.pack(side="left")

quantumTimeEntry=Entry(rowTwoFrame, state="disabled")
quantumTimeEntry.config(state="disabled")
quantumTimeEntry.pack(side="left")




inputFileLabel=Label(rowOneFrame,text="Input: ")
inputFileLabel.pack(side="left")

inputFileNameEntry=Entry(rowOneFrame)
inputFileNameEntry.pack(side="left",padx=(0,15),pady=10)

chooseAlgoLabel = Label(rowOneFrame, text="Algorithm: ")
chooseAlgoLabel.pack(side="left")
algorithmList = ["HPF", "FCFS", "RR", "SRTN"]
dropVar = StringVar()
dropVar.set("HPF")
algoritmMenu = OptionMenu(rowOneFrame, dropVar, *algorithmList, command=partial( updateParams,quantumTimeEntry))
#print(selectedAlgorithm)
algoritmMenu.pack(side="left",padx=(0,15),pady=10)

contextSwitchingTimeLabel = Label(rowOneFrame, text="Context Switch Time: ")
contextSwitchingTimeLabel.pack(side="left")

contextSwitchingTimeEntry=Entry(rowOneFrame)
contextSwitchingTimeEntry.pack(side="left",padx=(0,8),pady=10)


'''canvas = FigureCanvasTkAgg(figurePlotter, master=rowFourFrame)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, rowFourFrame)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)'''


generatorInfoButton=Button(rowThreeFrame,text="Generate Processess",command=lambda: generateProcessess(root))
generatorInfoButton.pack(side="left",padx=(0,300))
simulateButton=Button(rowThreeFrame,text= "Start Simulation",
	command= lambda:runAlgorithm(inputFileNameEntry.get(),outputFileNameEntry.get(),quantumTimeEntry.get(),contextSwitchingTimeEntry.get()))
simulateButton.pack(side="left")




'''def on_key_press(event):
	print("you pressed {}".format(event.key))
	key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)'''

root.mainloop()

