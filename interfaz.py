from Tkinter import *
import threading
import time 
from time import time
import sensores

sensores=sensores.Sensores()

class Interfaz:
    esc1t = None
    esc2t = None
    esc3t = None
    esd1t = None
    esd2t = None
    esd3t = None
    es1t = None
    es2t = None
    es3t = None

    def __init__(self):
        V = Tk()
        V.geometry('500x300')
        V.configure(bg = 'beige')
        V.title('Sensores')
        self.es1t = StringVar()
        self.es2t = StringVar()
        self.es3t = StringVar()
        self.esc1t = StringVar()
        self.esc2t = StringVar()
        self.esc3t = StringVar()
        self.esd1t = StringVar()
        self.esd2t = StringVar()
        self.esd3t = StringVar()
        self.entradas(V)
        self.labels(V)
        self.botones(V)
        V.mainloop()

    def CS1(self):
        cs1 = threading.Thread(target=self.countCS1)
        cs1.start()

    def CS2(self):
        cs2 = threading.Thread(target=self.countCS2)
        cs2.start()

    def CS3(self):
        cs3 = threading.Thread(target=self.countCS3)
        cs3.start()

    def DS1(self):
        ds1 = threading.Thread(target=self.countDS1)
        ds1.start()

    def DS2(self):
        ds2 = threading.Thread(target=self.countDS2)
        ds2.start()

    def DS3(self):
        ds3 = threading.Thread(target=self.countDS3)
        ds3.start()

    def countCS1(self):
        i=0
        self.esc1t.set(str(0))
        self.es1t.set(str(0))
        start_time = time()
        while i<20000:
            
            readt=sensores.readT(1)
            if readt>0:
                elapsed_time = time() - start_time
                self.esc1t.set(str(elapsed_time))
                self.es1t.set(str(readt))
                i=20000
                
    def countCS2(self):
        i=0
        while i<20000:
            time.sleep(0.001)
            self.esc2t.set(str(i))
            i=i+1
        self.esc2t.set(str(0))
    def countCS3(self):
        i=0
        while i<20000:
            time.sleep(0.001)
            self.esc3t.set(str(i))
            i=i+1
        self.esc3t.set(str(0))

    def countDS1(self):
        i=0
        start_time = time()
        while i<20000:
            readt=sensores.readT(1)
            if readt==0:
                elapsed_time = time() - start_time
                self.esc1t.set(str(elapsed_time))
                self.es1t.set(str(readt))
                i=20000

    def countDS2(self):
        i=0
        while i<20000:
            time.sleep(0.001)
            self.esd2t.set(str(i))
            i=i+1
        self.esd2t.set(str(0))
    def countDS3(self):
        i=0
        while i<20000:
            time.sleep(0.001)
            self.esd3t.set(str(i))
            i=i+1
        self.esd3t.set(str(0))
    

    def entradas(self,V):
        i=0
        self.es1t.set(str(i))
        self.es2t.set(str(i))
        self.es3t.set(str(i))

        self.esc1t.set(str(i))
        self.esc2t.set(str(i))
        self.esc3t.set(str(i))

        self.esd1t.set(str(i))
        self.esd2t.set(str(i))
        self.esd3t.set(str(i))

        eS1 = Entry(V, width=10,textvariable=self.es1t)
        eS1 .grid(row=0, column=1, padx=5, pady=5)
        eS1 .config(justify="right", state='readonly')
         
        eS2 = Entry(V, width=10,textvariable=self.es2t)
        eS2 .grid(row=1, column=1, padx=5, pady=5)
        eS2 .config(justify="right", state='readonly')
         
        eS3 = Entry(V, width=10,textvariable=self.es3t)
        eS3 .grid(row=2, column=1, padx=5, pady=5)
        eS3 .config(justify="right", state='readonly')

        eSC1 = Entry(V, width=8,textvariable=self.esc1t)
        eSC1 .grid(row=0, column=3, padx=5, pady=5)
        eSC1 .config(justify="right", state='readonly')
         
        eSC2 = Entry(V, width=8,textvariable=self.esc2t)
        eSC2 .grid(row=1, column=3, padx=5, pady=5)
        eSC2 .config(justify="right", state='readonly')
         
        eSC3 = Entry(V, width=8,textvariable=self.esc3t)
        eSC3 .grid(row=2, column=3, padx=5, pady=5)
        eSC3 .config(justify="right", state='readonly')

        eSD1 = Entry(V, width=8,textvariable=self.esd1t)
        eSD1 .grid(row=0, column=5, padx=5, pady=5)
        eSD1 .config(justify="right", state='readonly')
         
        eSD2 = Entry(V, width=8,textvariable=self.esd2t)
        eSD2 .grid(row=1, column=5, padx=5, pady=5)
        eSD2 .config(justify="right", state='readonly')
         
        eSD3 = Entry(V, width=8,textvariable=self.esd3t)
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
        b1=Button(V, text="CS1",command=self.CS1)
        b1.grid(row=0, column=2, padx=5, pady=5)

        b2=Button(V, text="CS2",command=self.CS2)
        b2.grid(row=1, column=2, padx=5, pady=5)

        b3=Button(V, text="CS3",command=self.CS3)
        b3.grid(row=2, column=2, padx=5, pady=5)

        b1=Button(V, text="DS1",command=self.DS1)
        b1.grid(row=0, column=4, padx=5, pady=5)

        b2=Button(V, text="DS2",command=self.DS2)
        b2.grid(row=1, column=4, padx=5, pady=5)

        b3=Button(V, text="DS3",command=self.DS3)
        b3.grid(row=2, column=4, padx=5, pady=5)

    