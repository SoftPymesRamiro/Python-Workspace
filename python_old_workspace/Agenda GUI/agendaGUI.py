from tkinter import *
import modulos

f = Frame(height=300,width=300) #Marco de la aplicacion #,cursor="circle"
f.pack(padx=15,pady=15)

logoimg = PhotoImage(file="b.gif")
etiquetalogo = Label(f,image = logoimg)
etiquetalogo.pack(side=TOP,padx=10,pady=10)

titulo = Label(f,text="Agenda Telefónica",fg="red",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

titulo = Label(f,text="Ramiro Andrés Bedoya",fg="red")
titulo.pack(side=TOP,padx=10,pady=10)

campo = Entry(f,textvariable = 5)
campo.pack(side=TOP,padx=10,pady=10)

boton1 = Button(f,text="Listar elementos de la agenda",command=lambda:modulos.listar(int(Entry.get(campo))))
boton1.pack(side=BOTTOM,padx=10,pady=10)

lista = Listbox(f)
lista.pack(side=TOP,padx=10,pady=10)
