from Tkinter import * 

 


class Interfaz:
   

    def __init__(self):
        V = Tk()
        V.geometry('400x300')
        V.configure(bg = 'beige')
        V.title('Sensores')
        entrada = Entry(V)
        entrada .grid(row=0, column=1, padx=5, pady=5)
        entrada .config(justify="right", state="normal")



        V.mainloop()

        
        

