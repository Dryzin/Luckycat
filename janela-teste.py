from tkinter import *

#criar janela

root = Tk()

bg = PhotoImage(file = "fundo.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

root.geometry("700x1000")
root.minsize(700, 1000)
root.maxsize(700, 1000)
#geometria


#criar os widgets

lb0 = Label(root, text='Nome:')
in0 = Entry(root, text='')
lb1 = Label(root, text='CPF:')
in1 = Entry(root, text='')
lb2 = Label(root, text='Telefone:')
in2 = Entry(root, text='')
bt0 = Button(root, text='Salvar')
bt1 = Button(root, text='Voltar')


#organizar os widgets

lb0.place(x= 180, y= 450)
in0.place(x= 250, y= 450)
lb1.place(x= 180, y= 550)
in1.place(x= 250, y= 550)
lb2.place(x= 180, y= 650)
in2.place(x= 250, y= 650)
bt0.place(x=180, y= 750)
bt1.place(x=250, y=750)


#executar a janela
root.mainloop()

#