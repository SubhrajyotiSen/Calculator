# -*- coding: utf-8 -*-
from Tkinter import *
import math

class Calc:

	#handle normal button clicks
	def action(self,arguement):
		if self.invalid == True:	#check if invalid error is being shown
			self.clearAll();
			self.invalid = False;
		self.entry.insert(END,arguement)

	#clear the entire expression
	def clearAll(self):
		self.entry.delete(0,END)

	#clear last character from expression
	def delete1(self):
		text = self.entry.get()[:-1]	#obtain expression excluding last character
		self.clearAll()					#clear the expression
		self.entry.insert(0,text)		#print expression excluding last character

	#evaluate the expression
	def calculate(self):
		try:
			value = eval(self.entry.get())
		except SyntaxError, e :			#check for improper syntax in expression
			self.invalidError()
		except ZeroDivisionError, e:	#check for divide by zero error
			self.invalidError()
		else:
			self.clearAll()
			self.entry.insert(0,value)
		
	#find square of a value/expression
	def square(self):
		try:
			value = eval(self.entry.get())
		except Exception, e:
			self.invalidError()
		else:
			newValue = math.pow(value,2)
			self.clearAll()
			self.entry.insert(0,newValue)

	#find square root of a value/expression
	def squareRoot(self):
		try:
			value = eval(self.entry.get())
		except Exception, e:
			self.entry.delete(0,END)
			self.entry.insert(0,"Invalid Input")
			self.invalid = True
		else:
			try:
				newValue = math.sqrt(value)
			except ValueError, e:		#mainly to check for attempts to get square root of negative number
				self.invalidError()
			else:
				self.clearAll()
				self.entry.insert(0,newValue)
	
	#handle cases of invalid error		
	def invalidError(self):
		self.entry.delete(0,END)
		self.entry.insert(0,"Invalid Input")
		self.invalid = True

		
	#just the init function (for lack of a better comment)
	def __init__(self,master):

		master.title("Calculator")
		master.geometry()

		self.entry = Entry(master)
		self.entry.grid(row=0,column=0,columnspan=6,pady=4)
		self.entry.focus_set()		#request focus on entry field

		#row 1 buttons
		Button(root, text="7",width=3,command=lambda:self.action(7)).grid(row=1,column=0)
		Button(root, text="8",width=3,command=lambda:self.action(8)).grid(row=1,column=1)
		Button(root, text="9",width=3,command=lambda:self.action(9)).grid(row=1,column=2)
		Button(root, text="x",width=3,command=lambda:self.action('*')).grid(row=1,column=3)
		Button(root, text="÷",width=3,command=lambda:self.action('/')).grid(row=1,column=4)
		Button(root, text="x²",width=3,command=lambda:self.square()).grid(row=1,column=5)

		#row 2 buttons
		Button(root, text="4",width=3,command=lambda:self.action(4)).grid(row=2,column=0)
		Button(root, text="5",width=3,command=lambda:self.action(5)).grid(row=2,column=1)
		Button(root, text="6",width=3,command=lambda:self.action(6)).grid(row=2,column=2)
		Button(root, text="+",width=3,command=lambda:self.action('+')).grid(row=2,column=3)
		Button(root, text="-",width=3,command=lambda:self.action('-')).grid(row=2,column=4)
		Button(root, text="√",width=3,command=lambda:self.squareRoot()).grid(row=2,column=5)

		#row 3 buttons
		Button(root, text="1",width=3,command=lambda:self.action(1)).grid(row=3,column=0)
		Button(root, text="2",width=3,command=lambda:self.action(2)).grid(row=3,column=1)
		Button(root, text="3",width=3,command=lambda:self.action(3)).grid(row=3,column=2)
		Button(root, text="(",width=3,command=lambda:self.action('(')).grid(row=3,column=4)
		Button(root, text=")",width=3,command=lambda:self.action(')')).grid(row=3,column=5)
		Button(root, text="AC",width=3,command=lambda:self.clearAll()).grid(row=3,column=3)
		
		#row 4 buttons
		Button(root, text="0",width=3,command=lambda:self.action(0)).grid(row=4,column=0)
		Button(root, text=".",width=3,command=lambda:self.action('.')).grid(row=4,column=1)
		Button(root, text="%",width=3,command=lambda:self.action('%')).grid(row=4,column=2)
		Button(root, text="DEL",width=3,command=lambda:self.delete1()).grid(row=4,column=3)
		Button(root, text="=",width=9,command=lambda:self.calculate()).grid(row=4,column=4,columnspan=2)

	

root = Tk()
calculator = Calc(root)
calculator.invalid = False  #flag to check if error is shown
root.mainloop()