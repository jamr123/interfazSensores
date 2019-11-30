from Tkinter import * 

class Interfaz:
   

    def __init__(self):
        V = Tk()
        V.geometry('600x300')
        V.configure(bg = 'beige')
        V.title('Sensores')
        self.entradas(V)
        self.labels(V)
        self.botones(V)
        V.mainloop()

    def entradas(self,V):

        eS1 = Entry(V)
        eS1 .grid(row=0, column=1, padx=5, pady=5)
        eS1 .config(justify="right", state='readonly')
         
        eS2 = Entry(V)
        eS2 .grid(row=1, column=1, padx=5, pady=5)
        eS2 .config(justify="right", state='readonly')
         
        eS3 = Entry(V)
        eS3 .grid(row=2, column=1, padx=5, pady=5)
        eS3 .config(justify="right", state='readonly')

        eSC1 = Entry(V)
        eSC1 .grid(row=0, column=3, padx=5, pady=5)
        eSC1 .config(justify="right", state='readonly')
         
        eSC2 = Entry(V)
        eSC2 .grid(row=1, column=3, padx=5, pady=5)
        eSC2 .config(justify="right", state='readonly')
         
        eSC3 = Entry(V)
        eSC3 .grid(row=2, column=3, padx=5, pady=5)
        eSC3 .config(justify="right", state='readonly')

        eSD1 = Entry(V)
        eSD1 .grid(row=0, column=5, padx=5, pady=5)
        eSD1 .config(justify="right", state='readonly')
         
        eSD2 = Entry(V)
        eSD2 .grid(row=1, column=5, padx=5, pady=5)
        eSD2 .config(justify="right", state='readonly')
         
        eSD3 = Entry(V)
        eSD3 .grid(row=2, column=5, padx=5, pady=5)
        eSD3 .config(justify="right", state='readonly')

        
        
        
    def labels(self,V):
        label = Label(V, text="S1")
        label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        label = Label(V, text="S2")
        label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        label = Label(V, text="S3")
        label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    
    def botones(self,V):
        b1=Button(V, text="Conectar S1")
        b1.grid(row=0, column=2, padx=5, pady=5)

        b2=Button(V, text="Conectar S2")
        b2.grid(row=1, column=2, padx=5, pady=5)

        b3=Button(V, text="Conectar S3")
        b3.grid(row=2, column=2, padx=5, pady=5)

        b1=Button(V, text="Desconectar S1")
        b1.grid(row=0, column=4, padx=5, pady=5)

        b2=Button(V, text="Desconectar S2")
        b2.grid(row=1, column=4, padx=5, pady=5)

        b3=Button(V, text="Desconectar S3")
        b3.grid(row=2, column=4, padx=5, pady=5)

    