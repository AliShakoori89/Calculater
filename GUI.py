from tkinter import * 
import Main

global expression
expression = ""
class BotGUI():

    def __init__(self,master):
        self.equation = StringVar()
        master.title('Calculator') 
        master.geometry("245x180") 
        expression_field = Entry(master,textvariable=self.equation,bg="light gray",width=40)
        expression_field.grid(row=0,column=0,columnspan=4,padx=1,pady=5) 
        self.equation.set('enter your expression') 

    def press(self,m):
        global expression 
        self.m=m   
        expression = expression + str(self.m)
        self.equation.set(expression)

    def square(self):
        global expression
        total=str((eval(expression))**0.5)
        self.equation.set(total)
        expression = ""

    def exponent(self):
        global expression
        total=str((eval(expression))**2)
        self.equation.set(total)
        expression = ""

    def one_div_x(self):
        global expression
        total=str(1/(eval(expression)))
        self.equation.set(total)
        expression = ""

    def equalpress(self): 
        try:   
            global expression
            total = str(eval(expression)) 
            self.equation.set(total) 
            expression = "" 
        except: 
            self.equation.set(" error ") 
            expression = "" 

    def clear(self): 
        global expression
        expression = "" 
        self.equation.set("")    