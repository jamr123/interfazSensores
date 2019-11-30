from Tkinter import *
import threading
import time 

class Interfaz:
    eS1=None
    eS2=None
    eS3=None
    eCS1=None
    eCS2=None
    eCS3=None
    eDS1=None
    eDS2=None
    eDS3=None

    def __init__(self):
        V = Tk()
        V.geometry('500x300')
        V.configure(bg = 'beige')
        V.title('Sensores')
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
        while i<10:
            time.sleep(1)
            self.eS1.delete(0,END)
            self.eS1.insert(0,str(i))
            i=i+1
    def countCS2(self):
        i=0
        while i<10:
            time.sleep(1)
            print(i)
            i=i+1
    def countCS3(self):
        i=0
        while i<10:
            time.sleep(1)
            print(i)
            i=i+1
    def countDS1(self):
        i=0
        while i<10:
            time.sleep(1)
            print(i)
            i=i+1
    def countDS1(self):
        i=0
        while i<10:
            time.sleep(1)
            print(i)
            i=i+1
    def countDS3(self):
        i=0
        while i<10:
            time.sleep(1)
            print(i)
            i=i+1
    

      

    def entradas(self,V):

        self.eS1 = Entry(V, width=10)
        self.eS1 .grid(row=0, column=1, padx=5, pady=5)
        self.eS1 .config(justify="right", state='readonly')
         
        self.eS2 = Entry(V, width=10)
        self.eS2 .grid(row=1, column=1, padx=5, pady=5)
        self.eS2 .config(justify="right", state='readonly')
         
        self.eS3 = Entry(V, width=10)
        self.eS3 .grid(row=2, column=1, padx=5, pady=5)
        self.eS3 .config(justify="right", state='readonly')

        self.eSC1 = Entry(V, width=8)
        self.eSC1 .grid(row=0, column=3, padx=5, pady=5)
        self.eSC1 .config(justify="right", state='readonly')
         
        self.eSC2 = Entry(V, width=8)
        self.eSC2 .grid(row=1, column=3, padx=5, pady=5)
        self.eSC2 .config(justify="right", state='readonly')
         
        self.eSC3 = Entry(V, width=8)
        self.eSC3 .grid(row=2, column=3, padx=5, pady=5)
        self.eSC3 .config(justify="right", state='readonly')

        self.eSD1 = Entry(V, width=8)
        self.eSD1 .grid(row=0, column=5, padx=5, pady=5)
        self.eSD1 .config(justify="right", state='readonly')
         
        self.eSD2 = Entry(V, width=8)
        self.eSD2 .grid(row=1, column=5, padx=5, pady=5)
        self.eSD2 .config(justify="right", state='readonly')
         
        self.eSD3 = Entry(V, width=8)
        self.eSD3 .grid(row=2, column=5, padx=5, pady=5)
        self.eSD3 .config(justify="right", state='readonly')

              
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

    