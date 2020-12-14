from tkinter import *
from tkinter import ttk 
import Arithmetic
import Display

class UnitConversion:
    def __init__(self,master,disp):
        self.operator = disp.operator
        self.textin= disp.textin
        

        group = LabelFrame(master, text="Unit Conversion", padx=15, pady=15)
        group.place(x=335,y=300)

        self.butconvert=Button(group,padx=10,pady=6,bd=4,bg='green',text="Convert",fg='yellow',command=lambda:self.convert(self.textin.get()),font=("Courier New",16,'bold'))
        #self.butconvert.place(x=10,y=450)
        self.butconvert.pack()

        self.variable = StringVar(group)
        self.variable.set("Feet to Meter")
        self.w = OptionMenu(group,self.variable, "Feet to Meter","Meter to Feet")
        self.w.configure(width=15, height=2)
        #self.w.place(x=200,y=450)
        self.w.pack()
        

    def convert(self,num):
        choice=self.variable.get()
        if(choice == "Feet to Meter"):
            self.FeetToMeter(num)
        else:
            self.MeterToFeet(num)


    def FeetToMeter(self,num):
        try:
            val = 0.3048*float(self.textin.get())
            self.textin.set("")
            self.textin.set(str(round(val,4))+" m")
            self.operator=""
            #self.textin.set("")
            #val=self.textin.get()
            #print(num)
           
        except:
            self.textin.set("Enter valid value")

    def MeterToFeet(self,num):
        try:
            val = 3.2804*float(self.textin.get())
            #val=self.textin.get()
            self.textin.set(str(round(val,4))+" f")
        except:
            self.textin.set("Enter valid value")
            