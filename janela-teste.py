from tkinter import *
from funcoes import *
#criar janela
obj_funcoes=funcoes()
root = Tk()

bg = PhotoImage(file = "4.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

root.geometry("700x1000")
root.minsize(707, 1000)
root.maxsize(707, 1000)
#geometria


#criar os widgets

lb0 = Label(root, text='Nome:')
in0 = Entry(root, text='')
lb1 = Label(root, text='CPF:')
in1 = Entry(root, text='')
lb2 = Label(root, text='Telefone:')
in2 = Entry(root, text='')
bt0 = Button(root, text='Salvar', command=lambda: obj_funcoes.cadastrar_participante(in1.get(),in0.get(),in2.get()))
bt1 = Button(root, text='Voltar')


#organizar os widgets

lb0.place(x= 90, y= 180)
in0.place(x= 250, y= 180)
lb1.place(x= 90, y= 230)
in1.place(x= 250, y= 230)
lb2.place(x= 90, y= 280)
in2.place(x= 250, y= 280)
bt0.place(x=350, y= 850)
bt1.place(x=90, y=850)


#executar a janela
root.mainloop()

#