from tkinter import *

#criar janela

root = Tk()

#criar os widgets

bt1 = Button(root, text='Bt1')
bt2 = Button(root, text='Bt2')
bt3 = Button(root, text='Bt3')
bt4 = Button(root, text='Bt4')


#organizar os widgets

bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)
bt3.grid(row=1, column=0, columnspan=3, sticky=NSEW)
bt4.grid(row=2, column=0, columnspan=3, sticky=NSEW)

#executar a janela
root.mainloop()

tetstst