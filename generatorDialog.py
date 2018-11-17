from generator import Generator
import os
from tkinter import *


class GeneratorDialog:
	def __init__(self,root):
		top = self.top = Toplevel(root)
		self.rowOneFrame=Frame(top)
		self.rowOneFrame.pack()
		self.rowTwoFrame=Frame(top)
		self.rowTwoFrame.pack()
		self.rowThreeFrame=Frame(top)
		self.rowThreeFrame.pack()

		self.inputFileNameLabel=Label(self.rowOneFrame,text="Input File Name: ")
		self.inputFileNameLabel.pack(side="left")
		self.inputFileNameEntry=Entry(self.rowOneFrame)
		self.inputFileNameEntry.pack(side="left")

		self.outputFileNameLabel=Label(self.rowTwoFrame,text="Output File Name: ")
		self.outputFileNameLabel.pack(side="left")
		self.outputFileNameEntry=Entry(self.rowTwoFrame)
		self.outputFileNameEntry.pack(side="left")

		self.generateButton=Button(self.rowThreeFrame,text="Generate",command=self.generate)
		self.generateButton.pack(side="left")

		self.cancelButton=Button(self.rowThreeFrame,text="Cancel",command=self.cancel)
		self.cancelButton.pack(side="left")

	def generate(self):
	 	if(self.inputFileNameEntry.get()=="" or self.outputFileNameEntry.get()==""):
	 		messagebox.showinfo("Error","You Have to specify an input file name and output file name ")
	 		return	
	 	exists = os.path.isfile(self.inputFileNameEntry.get())
 		if not(exists):
 			messagebox.showinfo("Error","Input file doesn't exist")
 			return
	 	processGenerator = Generator()
	 	processGenerator.generate_processes(self.inputFileNameEntry.get(),self.outputFileNameEntry.get())
	 	self.top.destroy()
		 	

	def cancel(self):
		self.top.destroy()  	


