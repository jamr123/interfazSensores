from Tkinter import * 

 


class Interfaz:
   

    def __init__(self):
        V = Tk()
        V.geometry('400x300')
        V.configure(bg = 'beige')
        V.title('Sensores')
        self.entradas(V)
        self.labels(V)
        

        V.mainloop()

    def entradas(self,V):

        eS1 = Entry(V)
        eS1 .grid(row=0, column=1, padx=5, pady=5)
        eS1 .config(justify="right", state='readonly')
         
        eS2 = Entry(V)
        eS2 .grid(row=2, column=1, padx=5, pady=5)
        eS2 .config(justify="right", state='readonly')
         
        eS3 = Entry(V)
        eS3 .grid(row=3, column=1, padx=5, pady=5)
        eS3 .config(justify="right", state='readonly')
        
        
    def labels(self,V):
        label = Label(V, text="S1")
        label.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        label = Label(V, text="S2")
        label.grid(row=0, column=2, sticky="w", padx=5, pady=5)

        label = Label(V, text="S3")
        label.grid(row=0, column=3, sticky="w", padx=5, pady=5)
