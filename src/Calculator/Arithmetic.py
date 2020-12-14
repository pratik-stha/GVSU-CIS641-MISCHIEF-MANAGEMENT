from  tkinter import *
from itertools import groupby
import re
import Display

class Arithmetic():

     def __init__(self,master,disp):
         
          self.operator=disp.operator
          myFrame = Frame(master)
          myFrame.pack()
          self.textin=disp.textin  

          self.but7=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(7),text="7",font=("Courier New",16,'bold'))
          self.but7.place(x=10,y=100)

          self.but4=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(4),text="4",font=("Courier New",16,'bold'))
          self.but4.place(x=10,y=170)

          self.but1=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(1),text="1",font=("Courier New",16,'bold'))
          self.but1.place(x=10,y=240)

          self.but8=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(8),text="8",font=("Courier New",16,'bold'))
          self.but8.place(x=75,y=100)

          self.but5=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(5),text="5",font=("Courier New",16,'bold'))
          self.but5.place(x=75,y=170)

          self.but2=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(2),text="2",font=("Courier New",16,'bold'))
          self.but2.place(x=75,y=240)

          self.but9=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(9),text="9",font=("Courier New",16,'bold'))
          self.but9.place(x=140,y=100)

          self.but6=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(6),text="6",font=("Courier New",16,'bold'))
          self.but6.place(x=140,y=170)

          self.but3=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(3),text="3",font=("Courier New",16,'bold'))
          self.but3.place(x=140,y=240)

          self.but0=Button(master,padx=14,pady=14,bd=4,bg='white',command=lambda:self.clickbut(0),text="0",font=("Courier New",16,'bold'))
          self.but0.place(x=10,y=310)

          self.butdot=Button(master,padx=47,pady=14,bd=4,bg='white',command=lambda:self.clickbut("."),text=".",font=("Courier New",16,'bold'))
          self.butdot.place(x=75,y=310)

          self.butpl=Button(master,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:self.clickbut("+"),font=("Courier New",16,'bold'))
          self.butpl.place(x=205,y=100)

          self.butsub=Button(master,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:self.clickbut("-"),font=("Courier New",16,'bold'))
          self.butsub.place(x=205,y=170)

          self.butml=Button(master,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:self.clickbut("*"),font=("Courier New",16,'bold'))
          self.butml.place(x=205,y=240)

          self.butdiv=Button(master,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:self.clickbut("/"),font=("Courier New",16,'bold'))
          self.butdiv.place(x=205,y=310)

          self.butclear=Button(master,padx=14,pady=119,bd=4,bg='orange',fg='white',text="C",command=self.clrbut,font=("Courier New",16,'bold'))
          self.butclear.place(x=270,y=100)

          self.butequal=Button(master,padx=144,pady=14,bd=4,bg='white',command=self.equlbut,text="=",font=("Courier New",16,'bold'))
          self.butequal.place(x=10,y=380)

          

    #Test function: Just to test
     def helloCallBack(self,val):
          # tkMessageBox.showinfo("Hello Python", "Hello World")
          print(str(val))

     def clickbut(self,number):   #lambda:clickbut(1)
          #global operator
          self.operator=self.operator+str(number)
          self.textin.set(self.operator)

     def equlbut(self):
          #global operator
          try:
               self.checkError(self.operator)
               add=str(round(eval(self.operator),4))
               self.textin.set(add)
               self.operator=" "
          except:
               self.textin.set("Invalid input")

     def clrbut(self):
          #global operator
          self.textin.set("")
          self.operator=" "
     
     def checkError(self,str):
         
          x = re.findall("[(-/+*)]{2,}", str) 
          if x:
               raise Exception("Invalid input")
          
          


    