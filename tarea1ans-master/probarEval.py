import tkinter as tk
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def procesar(funcion):
    
    
    x = np.linspace(-100,2*np.pi,100)
    y = eval(funcion.get())
    ax.clear()
    ax.plot(x,y), ax.grid(True)
    ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
    ax.set_title('$y(x)=$')
    line.draw()

    

#--- Raiz ---
root = tk.Tk()
root.geometry('940x450')
root.title("Tkinter + Matplotlib")
#------------

#-- Frames ---
left_frame = tk.Frame(root)
left_frame.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.9)

right_frame = tk.Frame(root, bg='#C0C0C0', bd=1.5)
right_frame.place(relx=0.3, rely=0.05, relwidth=0.65, relheight=0.9)
#---------------

#--- Botones ---

RH = 0.19
funcion = tk.StringVar()
entry=tk.Entry(root, textvariable=funcion, exportselection=0, bg = "#FFF", fg = "#000",)
entry.grid(row=1, column=0, columnspan=3)
B0 = tk.Button(left_frame,text="SIN(4x)",command =lambda: procesar(funcion))
B0.place(relheight=RH, relwidth=1)


#------------

#--- Agregar figura ---
figure = plt.Figure(figsize=(5,6), dpi=100)
ax = figure.add_subplot(111)
ax.grid(True),ax.set_xlabel('$x$'),ax.set_ylabel('$y(x)$')
line = FigureCanvasTkAgg(figure, right_frame)
line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#----------------------

root.mainloop()