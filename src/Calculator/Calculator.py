
from tkinter import*
import Arithmetic
import UnitConversion
import Display
import Trigonometric

me=Tk()
me.geometry("515x460")
me.title("CALCULATOR APP")
me.resizable(width=False, height=False)
melabel = Label(me,text="CALCULATOR",bg='dark gray',font=("Courier New",30,'bold'))
melabel.pack(side=TOP)
me.config(background='Dark gray')




Disp = Display.Display(me)
Arith = Arithmetic.Arithmetic(me,Disp)
Conv = UnitConversion.UnitConversion(me,Disp)
Trig = Trigonometric.Trigonometric(me,Disp)

me.mainloop()

