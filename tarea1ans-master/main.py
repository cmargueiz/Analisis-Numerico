import os
import sys
import tkinter
from tkinter import ttk
from tkinter import messagebox
import seno, coseno, e , arcseno, arctan, cosh, ln, senh, unoSobrelodemas

if os.environ.get('DISPLAY', '') == '':
    #print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


# create main window
master = tkinter.Tk()
master.title("ANS135")



# Aqui empizan los modales para cada boton
def senx():
    sen = tkinter.Toplevel()
    sen.title("Calcular Sen(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = seno.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)
  

def cosx():
    cos = tkinter.Toplevel()
    cos.title("Calcular Cos(x)")
    cos.focus_get()
    cos.grab_set()
    cos.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(cos, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(cos, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(cos, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(cos, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(cos)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(cos, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(cos, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = coseno.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(cos, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(cos, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)


def ex():
    sen = tkinter.Toplevel()
    sen.title("Calcular e^(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = e.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())
     
    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def shx():
    sen = tkinter.Toplevel()
    sen.title("Calcular Senh(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = senh.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def chx():
    sen = tkinter.Toplevel()
    sen.title("Calcular Cosh(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = cosh.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def asx():
    messagebox.showinfo(message="Los valores de la incognita tiene que estar entre -1 y 1", title="INFORMACION IMPORTANTE")
    sen = tkinter.Toplevel()
    sen.title("Calcular arcSen(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = arcseno.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def lnx():
    messagebox.showinfo(message="Los valores de la incognita tiene que estar entre -1 y 1", title="INFORMACION IMPORTANTE")
    sen = tkinter.Toplevel()
    sen.title("Calcular Ln(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
    
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = ln.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())
    
    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def alx():
    messagebox.showinfo(message="Los valores de la incognita tiene que estar entre -1 y 1", title="INFORMACION IMPORTANTE")
    sen = tkinter.Toplevel()
    sen.title("Calcular 1/(1+x^2)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)
  
    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = unoSobrelodemas.calculo(cif.get(),va.get())
            
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
                
            res.set(round(lista[-1][1], int(cif.get())))
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)
    
    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)

def atx():
    messagebox.showinfo(message="Los valores de la incognita tiene que estar entre -1 y 1", title="INFORMACION IMPORTANTE")
    sen = tkinter.Toplevel()
    sen.title("Calcular arcTan(x)")
    sen.focus_get()
    sen.grab_set()
    sen.transient(master=master)
    va = tkinter.StringVar()
    cif = tkinter.StringVar()
    tkinter.Label(sen, text="Ingrese el numero de cifras significativas").grid(row=0, column=0, columnspan=3)
    CS = tkinter.Entry(sen, textvariable=cif, exportselection=0, bg = "#212121", fg = "#FFFFFF")
    CS.grid(row=1, column=0, columnspan=3)
    tkinter.Label(sen, text="Ingrese el valor de su incognita").grid(row=2, column=0, columnspan=3)
    X = tkinter.Entry(sen, textvariable=va,exportselection=0, bg = "#212121", fg = "#FFFFFF")
    X.grid(row=3, column=0, columnspan=3)
    tbl = ttk.Treeview(sen)
    tbl.grid(row=5, columnspan=3)
    tbl["columns"] = ("1", "2")
    tbl.heading('#0', text='iteracion')
    tbl.heading('1', text='Aproximacion')
    tbl.heading('2', text='Error aproximado(%)')
    tkinter.Label(sen, text= "Resultado").grid(row = 3, column=2)
    res = tkinter.StringVar()
    tkinter.Entry(sen, state = 'disabled', disabledforeground = "#000" , justify= 'center', textvariable = res).grid(row = 4, column=2)

    def calcular():
        if cif.get() != "" and va.get() != "":
            i=0
            lista = arctan.calculo(cif.get(),va.get())
            for elem in lista:
                tbl.insert("", i, text = elem[0], values = (elem[1], elem[2]))
                i=i+1
            res.set(round(lista[-1][1], int(cif.get())))                
        else:
            messagebox.showerror(message= "Los campos no deben estar vacios", title= "Error")
            CS.delete(first = 0)
            X.delete(first = 0)

    def limpiar():
        cif.set("")
        va.set("")
        res.set("")
        tbl.delete(*tbl.get_children())

    tkinter.Button(sen, text="CALCULAR",command = lambda: calcular(), bg="#0288D1", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=1)
    tkinter.Button(sen, text="LIMPIAR",command = lambda: limpiar(), bg="#FF5252", fg="#FFFFFF",activebackground="#E040FB").grid(row=4, column=0)
# fin de los modales de los botones


# make a buttons and label for the window
tkinter.Label(master, text="Haga click sobre el boton de la funcion que desea utilizar", fg = "#FFF", bg = "#FF5252").grid(row=0, column=0, columnspan=3)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="Sen(x)", command=senx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=1, column=0)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="Cos(x)", command=cosx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=2, column=0)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="e^x", command=ex,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=3, column=0)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="Senh(x)", command=shx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=1, column=1)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="Cosh(x)", command=chx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=2, column=1)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="arcSen(x)", command=asx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=3, column=1)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="ln(1+x)", command=lnx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=1, column=2)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="1/(1+x^2)", command=alx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=2, column=2)
tkinter.Button(master, bg="#03A9F4", fg="#FFFFFF", text="arcTan(x)", command=atx,
               height="10", width="25", activebackground="#E040FB", bd = 5).grid(row=3, column=2)


# Run forever!
master.mainloop()
