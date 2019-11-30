        
from tkinter   
from tkinter import ttk 


class Interfaz:
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Sensores')
        ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
        raiz.mainloop()

        
        

