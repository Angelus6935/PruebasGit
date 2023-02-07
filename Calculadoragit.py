#from PIL import Image,ImageTk

from tkinter import *
#from turtle import width


raiz = Tk()
raiz.title("Calculadora")


miFrame=Frame(raiz)
miFrame.pack()

#-----------------------------visor-----row 0


varVisor = StringVar()
miVisor = Entry(miFrame, textvariable=varVisor)
miVisor.grid(row="0", column="0", columnspan="8")
miVisor.config(bg="gray", fg="white", justify="right")

#-----------------------------------------funciones de los botones.

borrar = False

def funboton1():
    global borrar
    if borrar == True:
        varVisor.set("1")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "1")

def funboton2():
    global borrar
    if borrar == True:
        varVisor.set("2")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "2")

def funboton3():
    global borrar
    if borrar == True:
        varVisor.set("3")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "3")

def funboton4():
    global borrar
    if borrar == True:
        varVisor.set("4")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "4")

def funboton5():
    global borrar
    if borrar == True:
        varVisor.set("5")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "5")

def funboton6():
    global borrar
    if borrar == True:
        varVisor.set("6")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "6")


def funboton7():
    global borrar
    if borrar == True:
        varVisor.set("7")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "7")

def funboton8():
    global borrar
    if borrar == True:
        varVisor.set("8")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "8")

def funboton9():
    global borrar
    if borrar == True:
        varVisor.set("9")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "9")


def funboton0():
    global borrar
    if borrar == True:
        varVisor.set("0")
        borrar = False
    else:
        varVisor.set(varVisor.get() + "0")   

def funbotondiv():
    varVisor.set(varVisor.get() + "/")

def funbotonmul():
    varVisor.set(varVisor.get() + "*")

def funbotonsuma():
    varVisor.set(varVisor.get() + "+")

def funbotonresta():
    varVisor.set(varVisor.get() + "-")

def funbotonputo():
    varVisor.set(varVisor.get() + ".")

def funbotonigual():
    global borrar
    try:
        varVisor.set(eval(varVisor.get()))
    except ZeroDivisionError:
        varVisor.set("Error div zero")
    finally:
        borrar = True









# ----------------------------botones------------

#---------------------------------------------row 1

boton7 = Button(miFrame, text="7", width=4, command = funboton7 )
boton7.grid(row=1, column=0)

boton8 = Button(miFrame, text="8", width=4, command = funboton8)
boton8.grid(row=1, column=1)

boton9 = Button(miFrame, text="9", width=4, command = funboton9)
boton9.grid(row=1, column=2)

botondiv = Button(miFrame, text="/", width=4, command = funbotondiv)
botondiv.grid(row=1, column=3)

#---------------------------------------------row 2


boton4 = Button(miFrame, text="4", width=4, command = funboton4)
boton4.grid(row=2, column=0)

boton5 = Button(miFrame, text="5", width=4, command = funboton5)
boton5.grid(row=2, column=1)

boton6 = Button(miFrame, text="6", width=4, command = funboton6)
boton6.grid(row=2, column=2)

botonmul = Button(miFrame, text="*", width=4, command = funbotonmul)
botonmul.grid(row=2, column=3)

#---------------------------------------------row 3

boton1 = Button(miFrame, text="1", width=4, command = funboton1)
boton1.grid(row=3, column=0)

boton2 = Button(miFrame, text="2", width=4, command = funboton2)
boton2.grid(row=3, column=1)

boton3 = Button(miFrame, text="3", width=4, command = funboton3,)
boton3.grid(row=3, column=2)

botonresta = Button(miFrame, text="-", width=4, command = funbotonresta)
botonresta.grid(row=3, column=3)

#---------------------------------------------row 4

botonpunto = Button(miFrame, text=".", width=4, command = funbotonputo)
botonpunto.grid(row=4, column=0)

boton0 = Button(miFrame, text="0", width=4, command = funboton0)
boton0.grid(row=4, column=1)

botonsuma = Button(miFrame, text="+", width=4, command = funbotonsuma)
botonsuma.grid(row=4, column=3)

botonigual = Button(miFrame, text="=", width=4, command = funbotonigual)
botonigual.grid(row=4, column=2)



raiz.mainloop()

"""miframe=Frame(raiz, width="1000", height="600")
miframe.pack()

miImagen = ImageTk.PhotoImage(file="playa.jpg")
Label(miframe, image=miImagen).place(x=100, y=100)
raiz.mainloop()"""
