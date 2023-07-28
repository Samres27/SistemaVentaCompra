from tkinter import *
from tkinter import ttk
import time
class interfaz:
    def __init__(self):
        root=Tk()
        ti=time.time()
        root.title("ventas Siloh")
        root.geometry("600x400")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        self.ventanaPreciosHoy()
        root.state('zoomed')
       
        
        root.mainloop()
        
    def ventanaPreciosHoy(self):
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Ventana secundaria")
        ventana_secundaria.config(width=700, height=500)
        ventana_secundaria.attributes('-topmost',True)
        #ventana_secundaria.eval('tk::PlaceWindow . center')
        lsPollo=["Pollo","con Menudo","sin Menudo","Especial","piernaMus","Pecho","Ala","Filete","Rabadilla","Menudo"]
        lsHuevo=["Huevo","Primera","Segunda","Tercera","Cuarta","Espec","Extra"]
        #parte de crear los valores para pollo 
        
        entry1 = ttk.Entry(ventana_secundaria)
        entry2 = ttk.Entry(ventana_secundaria)
        entry3 = ttk.Entry(ventana_secundaria)
        entry4 = ttk.Entry(ventana_secundaria)
        entry5 = ttk.Entry(ventana_secundaria)
        entry6 = ttk.Entry(ventana_secundaria)
        entry7 = ttk.Entry(ventana_secundaria)
        entry8 = ttk.Entry(ventana_secundaria)
        entry9 = ttk.Entry(ventana_secundaria)
        
        entry10 = ttk.Entry(ventana_secundaria)
        entry11 = ttk.Entry(ventana_secundaria)
        entry12 = ttk.Entry(ventana_secundaria)
        entry13 = ttk.Entry(ventana_secundaria)
        entry14 = ttk.Entry(ventana_secundaria)
        entry15 = ttk.Entry(ventana_secundaria)
        
        
        # Posicionarla en la ventana.
        
        #posicion y labels pollo
        lab0=Label(ventana_secundaria,text=lsPollo[0])
        lab0.place(x=120,y=20)
        entry1.place(y=50, x=100)
        lab1=Label(ventana_secundaria,text=lsPollo[1])
        lab1.place(x=20,y=50)
        entry2.place(y=100, x=100)
        lab2=Label(ventana_secundaria,text=lsPollo[2])
        lab2.place(x=20,y=100)
        entry3.place(y=150, x=100)
        lab3=Label(ventana_secundaria,text=lsPollo[3])
        lab3.place(x=20,y=150)
        entry4.place(y=200, x=100)
        lab4=Label(ventana_secundaria,text=lsPollo[4])
        lab4.place(x=20,y=200)
        entry5.place(y=250, x=100)
        lab5=Label(ventana_secundaria,text=lsPollo[5])
        lab5.place(x=20,y=250)
        entry6.place(y=300, x=100)
        lab6=Label(ventana_secundaria,text=lsPollo[6])
        lab6.place(x=20,y=300)
        entry7.place(y=350, x=100)
        lab7=Label(ventana_secundaria,text=lsPollo[7])
        lab7.place(x=20,y=350)
        entry8.place(y=400, x=100)
        lab8=Label(ventana_secundaria,text=lsPollo[8])
        lab8.place(x=20,y=400)
        entry9.place(y=450, x=100)
        lab9=Label(ventana_secundaria,text=lsPollo[9])
        lab9.place(x=20,y=450)
        
        #posicion y labels huevo
        lab10=Label(ventana_secundaria,text=lsHuevo[0])
        lab10.place(x=420,y=20)
        entry10.place(y=50, x=400)
        lab11=Label(ventana_secundaria,text=lsHuevo[1])
        lab11.place(x=320,y=50)
        entry11.place(y=100, x=400)
        lab12=Label(ventana_secundaria,text=lsHuevo[2])
        lab12.place(x=320,y=100)
        entry12.place(y=150, x=400)
        lab13=Label(ventana_secundaria,text=lsHuevo[3])
        lab13.place(x=320,y=150)
        entry13.place(y=200, x=400)
        lab14=Label(ventana_secundaria,text=lsHuevo[4])
        lab14.place(x=320,y=200)  
        entry14.place(y=250, x=400)
        lab15=Label(ventana_secundaria,text=lsHuevo[5])
        lab15.place(x=320,y=250) 
        entry15.place(y=300, x=400)
        lab16=Label(ventana_secundaria,text=lsHuevo[6])
        lab16.place(x=320,y=300)        
        boton_cerrar = ttk.Button(
            ventana_secundaria,
            text="Guardar Precios", 
            command=ventana_secundaria.destroy
        )
        boton_cerrar.place(x=600, y=450)

            
l=interfaz()
