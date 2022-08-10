from tkinter import *
from funcoes import *

#criar janela

root = Tk()
root.title("密")
root.geometry("707x1000")
root.minsize(707, 1000) 
root.maxsize(707, 1000)

fr1 = Frame()
fr2 = Frame()


bg = PhotoImage(file = "2.png") 
lb1 = Label(fr1, image=bg).grid(row=0 , column=0, sticky=W)

#geometria

#fr1.grid(row=1, column=0, sticky=NSEW)

#criar os widgets
criar = PhotoImage(file = "criar.png") 
info = PhotoImage(file = "info.png")
cadastro = PhotoImage(file = "cadastro.png")
finalizar = PhotoImage(file = "finalizar.png")


bt1 = Button(fr1, bg='red',image=criar, activebackground="red").place( x= 220, y= 420)
bt2 = Button(fr1, text='Info', bg='red',image=info, activebackground="red").place(x= 220, y= 470)
bt3 = Button(fr1, text='Cadastrar Participantes', bg='red',image=cadastro, activebackground="red", command=lambda: [fr1.grid_remove(), fr2.grid(row=2, column=0)]).place(x= 220, y= 520)
bt4 = Button(fr1, text='Finalizar Sorteio', bg='red',image=finalizar, activebackground="red").place(x= 220, y= 570)
fr1.grid()



####FR2####
fr2.grid()

obj_funcoes=funcoes()

bg2 = PhotoImage(file = "4.png")
lb2 = Label(fr2, image = bg2).grid(row=0 , column=0, sticky=W)



#criar os widgets
nome = PhotoImage(file = "criar.png") 
CPF = PhotoImage(file = "info.png")
Telefone = PhotoImage(file = "cadastro.png")
Salvar = PhotoImage(file = "finalizar.png")

#criar os widgets

lb0 = Label(fr2, text='Nome:').place(x= 90, y= 180)
in0 = Entry(fr2, text='').place(x= 250, y= 180)
lb1 = Label(fr2, text='CPF:').place(x= 90, y= 230)
in1 = Entry(fr2, text='').place(x= 250, y= 230)
lb2 = Label(fr2, text='Telefone:').place(x= 90, y= 280)
in2 = Entry(fr2, text='').place(x= 250, y= 280)
bt0 = Button(fr2, text='Salvar', command=lambda: obj_funcoes.cadastrar_participante(in1.get(),in0.get(),in2.get())).place(x=350, y= 850)
bt1 = Button(fr2, text='Voltar').place(x=90, y=850)


#organizar os widgets

#lb0.place(x= 90, y= 180)
#in0.place(x= 250, y= 180)
#lb1.place(x= 90, y= 230)
#in1.place(x= 250, y= 230)
#lb2.place(x= 90, y= 280)
#in2.place(x= 250, y= 280)
#bt0.place(x=350, y= 850)
#bt1.place(x=90, y=850)












root.mainloop()
#from janela_teste import *
