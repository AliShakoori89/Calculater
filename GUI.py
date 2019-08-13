from tkinter import * 
import Main



global expression
expression = ""
class GUI_Functions():

    def __init__(self):
        equation = StringVar() 
        pass 

    def equalpress(self): 
        try:   
            equation = str(eval(expression)) 
            equation.set(total) 
            expression = "" 
        except: 
            equation.set(" error ") 
            expression = "" 

    def clear(self): 
        
        expression = "" 
        obj.set("")

    def press(self):
        global expression    
        #eqauation = StringVar()
        expression = expression + str(self)
        equation.set(expression)
        #print(expression)

class BotGUI(GUI_Functions):

    def __init__(self,master):
        master.title('Calculator') 
        master.geometry("245x160") 
        expression_field = Entry(master,textvariable=equation,bg="light gray",width=40)
        expression_field.grid(row=0,column=0,columnspan=4,padx=1,pady=5) 
        equation.set('enter your expression') 

        B=Button(master,text=' 9 ',activebackground="grey",command=lambda : BotGUI.press(9), height=1, width=7)
        B.grid(row=8, column=2)
        B=Button(master,text=' 8 ',activebackground="grey",command=lambda : BotGUI.press(8), height=1, width=7)
        B.grid(row=8, column=1) 
        B=Button(master,text=' 7 ',activebackground="grey",command=lambda : BotGUI.press(7), height=1, width=7)
        B.grid(row=8, column=0) 
        B=Button(master,text=' 6 ',activebackground="grey",command=lambda : BotGUI.press(6), height=1, width=7)
        B.grid(row=7, column=2) 
        B=Button(master,text=' 5 ',activebackground="grey",command=lambda : BotGUI.press(5), height=1, width=7)
        B.grid(row=7, column=1)
        B=Button(master,text=' 4 ',activebackground="grey",command=lambda : BotGUI.press(4), height=1, width=7)
        B.grid(row=7, column=0)  
        B=Button(master,text=' 3 ',activebackground="grey",command=lambda : BotGUI.press(3), height=1, width=7)
        B.grid(row=6, column=2)
        B=Button(master,text=' 2 ',activebackground="grey",command=lambda : BotGUI.press(2), height=1, width=7)
        B.grid(row=6, column=1)
        B=Button(master,text=' 1 ',activebackground="grey",command=lambda : BotGUI.press(1), height=1, width=7)
        B.grid(row=6, column=0) 
        B=Button(master,text=" √ ",activebackground="grey",command=lambda : BotGUI.press(" √ "), height=1, width=7)
        B.grid(row=5, column=0)
        B=Button(master,text=" x²",activebackground="grey",command=lambda : BotGUI.press(" x²"), height=1, width=7)
        B.grid(row=5, column=1)
        B=Button(master,text="1/x",activebackground="grey",command=lambda : BotGUI.press("1/x"), height=1, width=7)
        B.grid(row=5, column=2)
        B=Button(master,text=' + ',activebackground="grey",command=lambda : BotGUI.press(' + '), height=1, width=7)
        B.grid(row=5, column=3)
        B=Button(master,text=' - ',activebackground="grey",command=lambda : BotGUI.press(' - '), height=1, width=7)
        B.grid(row=6, column=3)
        B=Button(master,text=' * ',activebackground="grey",command=lambda : BotGUI.press(' * '), height=1, width=7)
        B.grid(row=7, column=3)
        B=Button(master,text=' / ',activebackground="grey",command=lambda : BotGUI.press(' / '), height=1, width=7)
        B.grid(row=8, column=3) 
        B=Button(master,text="  =  ",activebackground="grey",command=BotGUI.equalpress, height=1, width=34)
        B.place(x=0,y=135)
        clear = Button(master, text='Clear', fg='black', bg='red',activebackground="grey",command=BotGUI. clear, height=1, width=7)
        clear.grid(row=5, column=0)