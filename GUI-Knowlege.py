from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x500')
def Button2():
    text = 'มีเงินในบัญชี 1000 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
    
    
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=50,y=100)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)







    
    

GUI.mainloop()
