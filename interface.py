from tkinter import *
from janela_teste import *

#criar janela

root = Tk()
root.title("密")


bg = PhotoImage(file = "2.png") 
fr1 = Frame( root)
lb1 = Label(image=bg)
lb1.place(x = 0, y = 0) 


root.geometry("707x1000")
root.minsize(707, 1000) 
root.maxsize(707, 1000)
#geometria



#criar os widgets
criar = PhotoImage(file = "criar.png") 
info = PhotoImage(file = "info.png")
cadastro = PhotoImage(file = "cadastro.png")
finalizar = PhotoImage(file = "finalizar.png")


bt1 = Button(root, bg='red',image=criar, activebackground="red")
bt2 = Button(root, text='Info', bg='red',image=info, activebackground="red")
bt3 = Button(root, text='Cadastrar Participantes', bg='red',image=cadastro, activebackground="red", command=lambda: [teste, root.destroy()])
bt4 = Button(root, text='Finalizar Sorteio', bg='red',image=finalizar, activebackground="red")


#organizar os widgets

bt1.place(x= 220, y= 420)
bt2.place(x= 220, y= 470)
bt3.place(x= 220, y= 520)
bt4.place(x= 220, y= 570)

#executar a janela
root.mainloop()

