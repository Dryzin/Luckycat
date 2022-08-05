from tkinter import *

#criar janela

root = Tk()

bg = PhotoImage(file = "undo.png") 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 

root.geometry("700x1000")
root.minsize(700, 1000) 
root.maxsize(700, 1000)
#geometria


#criar os widgets

bt1 = Button(root, text='Novo Sorteio')
bt2 = Button(root, text='Ver Sorteio')
bt3 = Button(root, text='Cadastrar Participantes')
bt4 = Button(root, text='Finalizar Sorteio')


#organizar os widgets

bt1.place(x= 180, y= 450)
bt2.place(x= 280, y= 450)
bt3.place(x= 180, y= 550)
bt4.place(x= 180, y= 650)

#executar a janela
root.mainloop()

