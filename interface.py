from tkinter import *
from turtle import color
from funcoes import *

#criar janela
obj_funcoes=funcoes()


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

cadastro = PhotoImage(file = "cadastro.png")
finalizar = PhotoImage(file = "finalizar.png")


bt3 = Button(fr1, text='Cadastrar Participantes', bg='#d91a1a',image=cadastro, activebackground="#d91a1a", command=lambda: [fr1.grid_remove(), fr2.grid(row=2, column=0)]).place(x= 220, y= 420)
bt4 = Button(fr1, text='Finalizar Sorteio', bg='#d91a1a',image=finalizar, activebackground="#d91a1a").place(x= 220, y= 470)
fr1.grid()


####FR2####


bg2 = PhotoImage(file = "4.png")
lb2 = Label(fr2, image = bg2).grid(row=0 , column=0, sticky=W)


#criar os widgets
salvar = PhotoImage(file = "salvar.png")
jogar = PhotoImage(file = "jogar.png")
voltar = PhotoImage(file = "voltar.png")




#criar os widgets


in0 = Entry(fr2, bg= "#d91a1a")

in1 = Entry(fr2, bg= "#d91a1a")

in2 = Entry(fr2, bg= "#d91a1a")
bt0 = Button(fr2, text='Salvar', bg= "#d91a1a",activebackground="#d91a1a",image=salvar, command=lambda: obj_funcoes.cadastrar_participante(in1.get(),in0.get(),in2.get()))

bt1 = Button(fr2, text='Voltar', bg= "#d91a1a",activebackground="#d91a1a",image=voltar, command=lambda:[fr2.grid_remove(), fr1.grid(row=2, column=0)])


enS1 = Entry(fr2, text='', width=10, bg= "#d91a1a")

enS2 = Entry(fr2, text='', width=10, bg= "#d91a1a")
enS3 = Entry(fr2, text='', width=10, bg= "#d91a1a")
enS4 = Entry(fr2, text='', width=10, bg= "#d91a1a")
enS5 = Entry(fr2, text='', width=10, bg= "#d91a1a")

def sv_jogo():

    global jogo
    
    jogo = enS1.get()+enS2.get()+enS3.get()+enS4.get()+enS5.get()

    '''jogo.append(enS1.get())
    jogo.append(enS2.get())
    jogo.append(enS3.get())'''

    print (jogo)
    return

bt3 = Button(fr2, text='Jogar', command=lambda: [sv_jogo(), obj_funcoes.cadastrar_jogo(in1.get(), jogo)])

#print (jogo)


in0.place(x= 250, y= 90)

in1.place(x= 250, y= 170)

in2.place(x= 315, y= 250)

bt0.place(x=80, y= 350)

bt1.place(x=80, y=850)

bt3.place(x=211, y=850)

enS1.place(x= 53, y= 615)
enS2.place(x= 189, y= 615)
enS3.place(x= 325, y= 615)
enS4.place(x= 457, y= 615)
enS5.place(x= 593, y= 615)
root.mainloop()
#from janela_teste import 1*
