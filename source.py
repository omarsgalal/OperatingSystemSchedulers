import tkinter as tk
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, simpledialog,OptionMenu,Frame,messagebox
from functools import partial
selectedAlgorithm="HPF"

class process:
    def __init__(self,processNumber,arrivalTime,burstTime,priority):
        
        self.processNumber=processNumber
        self.arrivalTime=arrivalTime
        self.burstTime=burstTime
        self.priority=priority

def readProcesses(inputFileName):
	# read the process
	inputFile=open(inputFileName,'r')
	out=inputFile.readlines()
	currProcess=[]
	processNumber=out[0]
	processes=[]
	for line in out:
		currProcess=line.split()
		if(len(currProcess)==1):
			continue
		x=process(int(currProcess[0]),int(currProcess[1]),int(currProcess[2]),int(currProcess[3]))
		processes.append(x)
	return processes

def runAlgorithm(processes,quantumTimeEntry,contextSwitchingTimeEntry):
        
        print(selectedAlgorithm)
        #print(quantumTimeEntry)
        #print(contextSwitchingTimeEntry)
        if(not(contextSwitchingTimeEntry.isdigit()) or contextSwitchingTimeEntry==""):
            messagebox.showinfo("Error","Please Enter a positive context switching time ")
            return
                     
        if((not(quantumTimeEntry.isdigit()) or quantumTimeEntry=="" )and selectedAlgorithm=="RR"):
            messagebox.showinfo("Error","Please Enter a positive quantum Time ")
            return
        contextSwitchTime=int(contextSwitchingTimeEntry)
        if(selectedAlgorithm=="HPF"):
            print("HPF")
        if(selectedAlgorithm=="FCFS"):
            print("FCFS")
        if(selectedAlgorithm=="SRTN"):
            print("SRTN")
        if(selectedAlgorithm=="RR"):
            quantumTime=int(quantumTimeEntry.get()) 
            print("RR")           


def updateParams(quantumTimeEntry,value) :
    #print(value)
    #print(quantumTimeEntry)
    #print(selectedAlgorithm)
    global selectedAlgorithm
    selectedAlgorithm=value
    print(selectedAlgorithm)
    #print(quantumTimeEntry)
    
    if(value!="RR"):
        quantumTimeEntry.config(state="disabled")
    else:
        quantumTimeEntry.config(state="normal")



root = tk.Tk()
inputFileName = simpledialog.askstring("Input", "Please enter the Input file Name which is generated by the process generator ",
                                parent=root)
while inputFileName is None or inputFileName=="":
    inputFileName = simpledialog.askstring("Input", "You Have to enter the input file name generated by process generator",
                                parent=root)  
processes=readProcesses(inputFileName)
#selectedAlgorithm="HPF"
chooseAlgoFrame = Frame(root)
chooseAlgoFrame.pack()
        
quantumTimeFrame = Frame(root)
quantumTimeFrame.pack()

runAlgorithmFrame=Frame(root)
runAlgorithmFrame.pack()

        
contextTimeFrame = Frame(root)
contextTimeFrame.pack()


        
quantumLabel = Label(quantumTimeFrame, text="Quantum Time: ")
quantumLabel.pack(side="left")
quantumTimeEntry=Entry(quantumTimeFrame, state="disabled")
quantumTimeEntry.config(state="disabled")
quantumTimeEntry.pack()
quantumTimeFramePlace=quantumTimeFrame.place_info()

chooseAlgoLabel = Label(chooseAlgoFrame, text="Please choose an Algorithm: ")
chooseAlgoLabel.pack(side = "left")
algorithmList = ["HPF", "FCFS", "RR", "SRTN"]
dropVar = StringVar()
dropVar.set("HPF")
algoritmMenu = OptionMenu(chooseAlgoFrame, dropVar, *algorithmList, command=partial( updateParams,quantumTimeEntry))
#print(selectedAlgorithm)
algoritmMenu.pack(side="bottom")



contextSwitchingTimeLabel = Label(contextTimeFrame, text="context switching time:")
contextSwitchingTimeLabel.pack(side="left")
contextSwitchingTimeEntry=Entry(contextTimeFrame)
contextSwitchingTimeEntry.pack()

runAlgorithmButton=Button(text="Run",command= lambda:runAlgorithm(processes,quantumTimeEntry.get(),contextSwitchingTimeEntry.get()))
runAlgorithmButton.pack()
root.mainloop()

