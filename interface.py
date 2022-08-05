from tkinter import *

#criar janela

root = Tk()
root.title("密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密密")

bg = PhotoImage(file = "fundo.png") 
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0) 

root.geometry("707x1000")

#criar os widgets
bt = PhotoImage(file = "bt.png") 

bt1 = Button(root,bg='red' ,image=bt, activebackground="red")
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

