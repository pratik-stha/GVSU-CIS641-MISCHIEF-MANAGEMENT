from tkinter import *
import math
import Display

class Trigonometric:
    def __init__(self,master,disp):
        group = LabelFrame(master, text="Trigonometry", padx=15, pady=7)
        group.place(x=335,y=100)

        self.val = disp.textin
        #w = Label(group,text="Trigonometric")
        self.SineBut=Button(group,padx=37,pady=5,bd=4,bg='white',command=lambda:self.Sine(self.val.get()),text="Sin",font=("Courier New",16,'bold'))
        self.SineBut.pack()
        self.CosBut=Button(group,padx=37,pady=5,bd=4,bg='white',command=lambda:self.Cos(self.val.get()),text="Cos",font=("Courier New",16,'bold'))
        self.CosBut.pack()
        self.TanBut=Button(group,padx=37,pady=5,bd=4,bg='white',command=lambda:self.Tan(self.val.get()),text="Tan",font=("Courier New",16,'bold'))
        self.TanBut.pack()

        

    def Sine(self,x):
        try:
            result = math.sin(math.radians(float(x)))
            self.val.set(round(result,4))
        except:
            self.val.set("Invalid input")
    
    def Cos(self,x):
        try:
            result = math.cos(math.radians(float(x)))
            self.val.set(round(result,4))
        except:
            self.val.set("Invalid input")

    def Tan(self,x):
        try:
            if(float(x)==90 or float(x)==-90):
                raise Exception("Invalid input")
            result = math.tan(math.radians(float(x)))
            self.val.set(round(result,4))
        except:
            self.val.set("Invalid input")
           
        
       
