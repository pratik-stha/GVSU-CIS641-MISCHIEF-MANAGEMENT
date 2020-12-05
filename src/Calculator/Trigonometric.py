from tkinter import *
import math
import Display

class Trigonometric:
    def __init__(self,master,disp):
        group = LabelFrame(master, text="Trigonometric", padx=5, pady=5)
        group.place(x=350,y=100)

        self.val = disp.textin
        #w = Label(group,text="Trigonometric")
        self.SineBut=Button(group,padx=14,pady=5,bd=4,bg='white',command=lambda:self.Sine(self.val.get()),text="Sin",font=("Courier New",16,'bold'))
        self.SineBut.pack()
        self.CosBut=Button(group,padx=14,pady=5,bd=4,bg='white',command=lambda:self.Cos(self.val.get()),text="Cos",font=("Courier New",16,'bold'))
        self.CosBut.pack()
        self.TanBut=Button(group,padx=14,pady=5,bd=4,bg='white',command=lambda:self.Tan(self.val.get()),text="Tan",font=("Courier New",16,'bold'))
        self.TanBut.pack()

        

    def Sine(self,x):
        result = math.sin(math.radians(float(x)))
        self.val.set(result)
    
    def Cos(self,x):
        result = math.cos(math.radians(float(x)))
        self.val.set(result)

    def Tan(self,x):
        result = math.tan(math.radians(float(x)))
        self.val.set(result)
        
           
        
       
