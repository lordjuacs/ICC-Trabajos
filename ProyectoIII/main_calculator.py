from tkinter import *
from math import *
from funciones_derivadas import *
from funciones_integreles import *


def click(n):
    global operador
    operador = operador + str(n)
    input_text.set(operador)


def operacion():
    global operador
    try:
        opera = eval(operador)
    except:
        limpiarpantalla()
        opera = "MATH ERROR"
    input_text.set(opera)

def limpiarpantalla():
    global operador
    operador = ("")
    input_text.set(operador)

calculadora = Tk()
calculadora.title("H31D3Rfx-091201PE PLUS P.A.M.T")
calculadora.geometry("305x520")
calculadora.configure(background="slate gray")
input_text = StringVar()
operador = ""

boton7 = Button(calculadora, bd=2, text=7, width=5, height=1,bg="white",fg="gray",command=lambda:click(7)).place(x=10, y=60)
boton8 = Button(calculadora, bd=2, text=8, width=5, height=1,bg="white",fg="gray",command=lambda:click(8)).place(x=70, y=60)
boton9 = Button(calculadora, bd=2, text=9, width=5, height=1,bg="white",fg="gray",command=lambda:click(9)).place(x=130, y=60)
boton4 = Button(calculadora, bd=2, text=4, width=5, height=1,bg="white",fg="gray",command=lambda:click(4)).place(x=10, y=100)
boton5 = Button(calculadora, bd=2, text=5, width=5, height=1,bg="white",fg="gray",command=lambda:click(5)).place(x=70, y=100)
boton6 = Button(calculadora, bd=2, text=6, width=5, height=1,bg="white",fg="gray",command=lambda:click(6)).place(x=130, y=100)
boton1 = Button(calculadora, bd=2, text=1, width=5, height=1,bg="white",fg="gray",command=lambda:click(1)).place(x=10, y=140)
boton2 = Button(calculadora, bd=2, text=2, width=5, height=1,bg="white",fg="gray",command=lambda:click(2)).place(x=70, y=140)
boton3 = Button(calculadora, bd=2, text=3, width=5, height=1,bg="white",fg="gray",command=lambda:click(3)).place(x=130, y=140)
botonsuma = Button(calculadora, bd=2, text="+", width=5, height=1,bg="white",fg="gray",command=lambda:click("+")).place(x=190, y=60)
botonmulti = Button(calculadora, bd=2, text="x", width=5, height=1,bg="white",fg="gray".lower(),command=lambda:click("*")).place(x=190, y=100)
botonmenos = Button(calculadora, bd=2, text="-", width=5, height=1,bg="white",fg="gray",command=lambda:click("-")).place(x=250, y=60)
botondivision = Button(calculadora, bd=2, text="/", width=5, height=1,bg="white",fg="gray",command=lambda:click("/")).place(x=250, y=100)
boton0 = Button(calculadora, bd=2, text=0, width=5, height=1,bg="white",fg="gray",command=lambda:click(0)).place(x=10, y=180)
botondecimal = Button(calculadora, bd=2, text=".", width=5, height=1,bg="white",fg="gray",command=lambda:click(".")).place(x=70, y=180)
botonigual = Button(calculadora, bd=2, text="=", width=5, height=1,bg="white",fg="gray",command=operacion).place(x=250, y=260)
botoncuadrado = Button(calculadora, bd=2, text="x²", width=5, height=1,bg="white",fg="gray",command=lambda:click("**2")).place(x=190, y=140)
botoncubo = Button(calculadora, bd=2, text="xⁿ", width=5, height=1,bg="white",fg="gray",command=lambda:click("**")).place(x=250, y=140)
botonraiz = Button(calculadora, bd=2, text="√", width=5, height=1,bg="white",fg="gray",command=lambda:click("sqrt")).place(x=190, y=180)
botonpi = Button(calculadora, bd=2, text="π", width=5, height=1,bg="white",fg="gray",command=lambda:click("pi")).place(x=190, y=220)
botoncoma = Button(calculadora, bd=2, text=",", width=5, height=1,bg="white",fg="gray",command=lambda:click(",")).place(x=130, y=220)
botonparentesis1 = Button(calculadora, bd=2, text="(", width=5, height=1,bg="white",fg="gray",command=lambda:click("(")).place(x=10, y=220)
botonparentesis2 = Button(calculadora, bd=2, text=")", width=5, height=1,bg="white",fg="gray",command=lambda:click(")")).place(x=70, y=220)
botonlogaritmo = Button(calculadora, bd=2, text="ln", width=5, height=1,bg="white",fg="gray",command=lambda:click("log")).place(x=250, y=180)
botonlimpiar = Button(calculadora, bd=2, text="AC", width=5, height=1,bg="white",fg="gray",command=limpiarpantalla).place(x=190, y=260)
botonlogaritmo10 = Button(calculadora, bd=2, text="log", width=5, height=1,bg="white",fg="gray",command=lambda:click("log10")).place(x=250, y=220)
botontangente = Button(calculadora, bd=2, text="tan", width=5, height=1,bg="white",fg="gray",command=lambda:click("tan")).place(x=130, y=260)
botonseno = Button(calculadora, bd=2, text="sin", width=5, height=1,bg="white",fg="gray",command=lambda:click("sin")).place(x=10, y=260)
botoncoseno = Button(calculadora, bd=2, text="cos", width=5, height=1,bg="white",fg="gray",command=lambda:click("cos")).place(x=70, y=260)
finalboton = Button(calculadora, bd=2, text="e", width=5, height=1,bg="white",fg="gray",command=lambda:click("e")).place(x=130, y=180)

lbl = Label(calculadora, text="DERIVATIVE",bg="slate gray",fg="white", font="Times").place(x=10,y=300)

botonderivada1 = Button(calculadora, bd=2, text="d(xⁿ)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dxⁿ")).place(x=10, y=330)
botonderivada2 = Button(calculadora, bd=2, text="d(aˣ)", width=5, height=1,bg="white",fg="gray",command=lambda:click("daˣⁿ")).place(x=70, y=330)
botonderivada3 = Button(calculadora, bd=2, text="d(lnx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dlnx")).place(x=130, y=330)
botonderivada4 = Button(calculadora, bd=2, text="d(eˣ)", width=5, height=1,bg="white",fg="gray",command=lambda:click("deˣ")).place(x=190, y=330)
botonderivada5 = Button(calculadora, bd=2, text="d(sinx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dsinx")).place(x=250, y=330)
botonderivada6 = Button(calculadora, bd=2, text="d(cosx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dcosx")).place(x=10, y=370)
botonderivada7 = Button(calculadora, bd=2, text="d(tgx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dtgx")).place(x=70, y=370)
botonderivada8 = Button(calculadora, bd=2, text="d(cscx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dctgx")).place(x=130, y=370)
botonderivada9 = Button(calculadora, bd=2, text="d(secx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dsecx")).place(x=190, y=370)
botonderivada10 = Button(calculadora, bd=2, text="d(ctgx)", width=5, height=1,bg="white",fg="gray",command=lambda:click("dcscx")).place(x=250, y=370)

lbl = Label(calculadora, text="INTEGRAL",bg="slate gray",fg="white", font="Times").place(x=10,y=410)

botonintegral1 = Button(calculadora, bd=2, text="∫xⁿdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("ixⁿ")).place(x=10, y=440)
botonintegral2 = Button(calculadora, bd=2, text="∫aˣdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("iaˣ")).place(x=70, y=440)
botonintegral3 = Button(calculadora, bd=2, text="∫eˣdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("ieˣ")).place(x=130, y=440)
botonintegral4 = Button(calculadora, bd=2, text="∫dx/x", width=5, height=1,bg="white",fg="gray",command=lambda:click("i1entrex")).place(x=190, y=440)
botonintegral5 = Button(calculadora, bd=2, text="∫sinxdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("isinx")).place(x=250, y=440)
botonintegral6 = Button(calculadora, bd=2, text="∫cosxdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("icosx")).place(x=10, y=480)
botonintegral7 = Button(calculadora, bd=2, text="∫tgxdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("itgx")).place(x=70, y=480)
botonintegral8 = Button(calculadora, bd=2, text="∫ctgxdx", width=5, height=1,bg="white",fg="gray",command=lambda:click("ictg")).place(x=130, y=480)
botonintegral9 = Button(calculadora, bd=2, text="∫1/√1-x²", width=6, height=1,bg="white",fg="gray",command=lambda:click("i_1entresqrt1menosxcuadrado")).place(x=190, y=480)
botonintegral10 = Button(calculadora, bd=2, text="∫-1/√1-x²", width=6, height=1,bg="white",fg="gray",command=lambda:click("imenos1entresqrt1menosxcuadrado")).place(x=250, y=480)



e1 = Entry(calculadora,bd=10,width=44,justify="right",bg="white",fg="gray",state="disabled",textvariable=input_text)
e1.pack()
e1.place(x=10,y=10)
calculadora.mainloop()