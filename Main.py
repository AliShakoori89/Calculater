from tkinter import *
import GUI

expression = ""

class GUI_Functions():

    def __init__(self,parent):
        pass 

    def equalpress(self): 
        try: 
            global expression 
            equation = str(eval(expression)) 
            equation.set(total) 
            expression = "" 
        except: 
            equation.set(" error ") 
            expression = "" 

    def clear(self): 
        global expression 
        expression = "" 
        equation.set("")

    def press(self,num): 
        global expression 
        self.num=num
        #eqauation = StringVar()
        expression = expression + str(self.num)
        equation.set(expression)
        #print(expression)

if __name__ == "__main__":
    root = Tk()
    GUI_Frame = GUI.BotGUI(root)
    equation = StringVar()
    root.mainloop()
    