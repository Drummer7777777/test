import tkinter as tk
from calc_itog import *


def add_digit(digit):
    value=ent.get()+str(digit)
    ent.delete(0,tk.END)
    ent.insert(0,value)

def calculate():
    answer=parser(ent.get())
    ent.delete(0,tk.END)
    ent.insert(0,str(answer))

def delete_ent():
    ent.delete(0,tk.END)

win = tk.Tk()
win.title('Калькулятор')
win.config(bg='white')

ent=tk.Entry(win,font=('Arial',15),justify=tk.RIGHT)
btn1=tk.Button(win,text='1',height=4,width=5,bd=5,command=lambda:add_digit(1))
btn2=tk.Button(win,text='2',height=4,width=5,bd=5,command=lambda:add_digit(2))
btn3=tk.Button(win,text='3',height=4,width=5,bd=5,command=lambda:add_digit(3))
btn4=tk.Button(win,text='4',height=4,width=5,bd=5,command=lambda:add_digit(4))
btn5=tk.Button(win,text='5',height=4,width=5,bd=5,command=lambda:add_digit(5))
btn6=tk.Button(win,text='6',height=4,width=5,bd=5,command=lambda:add_digit(6))
btn7=tk.Button(win,text='7',height=4,width=5,bd=5,command=lambda:add_digit(7))
btn8=tk.Button(win,text='8',height=4,width=5,bd=5,command=lambda:add_digit(8))
btn9=tk.Button(win,text='9',height=4,width=5,bd=5,command=lambda:add_digit(9))
btn0=tk.Button(win,text='0',height=4,width=5,bd=5,command=lambda:add_digit(0))
btnpl=tk.Button(win,text='+',height=4,width=5,bd=5,command=lambda:add_digit('+'))
btnmin=tk.Button(win,text='-',height=4,width=5,bd=5,command=lambda:add_digit('-'))
btnumn=tk.Button(win,text='*',width=5,bd=5,command=lambda:add_digit('*'))
btndel=tk.Button(win,text='/',width=5,bd=5,command=lambda:add_digit('/'))
btnsko=tk.Button(win,text='(',width=5,bd=5,command=lambda:add_digit('('))
btnskz=tk.Button(win,text=')',width=5,bd=5,command=lambda:add_digit(')'))
btncl=tk.Button(win,text='Считать',bd=5,command=calculate)
btncalc=tk.Button(win,text='Отчистить',bd=5,command=delete_ent)

ent.grid(row=0,column=0,columnspan=5,stick='we')
btn1.grid(row=1,column=1,padx=5,pady=5)
btn2.grid(row=1,column=2,padx=5,pady=5)
btn3.grid(row=1,column=3,padx=5,pady=5)
btn4.grid(row=2,column=1,padx=5,pady=5)
btn5.grid(row=2,column=2,padx=5,pady=5)
btn6.grid(row=2,column=3,padx=5,pady=5)
btn7.grid(row=3,column=1,padx=5,pady=5)
btn8.grid(row=3,column=2,padx=5,pady=5)
btn9.grid(row=3,column=3,padx=5,pady=5)
btn0.grid(row=4,column=2,padx=5,pady=5)
btnpl.grid(row=4,column=1,padx=5,pady=5)
btnmin.grid(row=4,column=3,padx=5,pady=5)
btnumn.grid(row=3,column=0,rowspan=2,stick='ns',padx=5,pady=5)
btndel.grid(row=3,column=4,rowspan=2,stick='ns',padx=5,pady=5)
btnsko.grid(row=1,column=0,rowspan=2,stick='ns',padx=5,pady=5)
btnskz.grid(row=1,column=4,rowspan=2,stick='ns',padx=5,pady=5)
btncalc.grid(row=5,column=0,columnspan=5,stick='we',padx=5,pady=5)
btncl.grid(row=6,column=0,columnspan=5,stick='we',padx=5,pady=5)


win.mainloop()