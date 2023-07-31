from functools import partial   
from tkinter import *
from tkinter import ttk
import time
from ventas import *
class interfaz:
    def __init__(self):
        root=Tk()
        self.elementos=[]
        ti=time.time()
        root.title("ventas Siloh")
        root.geometry("600x400")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        #self.ventanaPreciosHoy()
        root.state('zoomed')
        self.ventanaRegistarCompra()
        
        root.mainloop()
        
    def ventanaPreciosHoy(self):
        ventana_secundaria = Toplevel()
        ventana_secundaria.title("Ventana secundaria")
        ventana_secundaria.config(width=700, height=700)
        ventana_secundaria.attributes('-topmost',True)
        #ventana_secundaria.eval('tk::PlaceWindow . center')
        lsPollo=["Pollo","P con Menud","P sin Menud","S con Menud","S sin Menud","Especial","PiernaMus",
                 "Pecho","Ala","Filete","Rabadilla","Menudo","Higado","Corazon","Hueso de Pecho","Molleja"]
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
        entry16 = ttk.Entry(ventana_secundaria)
        
        entryH0 = ttk.Entry(ventana_secundaria)
        entryH1 = ttk.Entry(ventana_secundaria)
        entryH2 = ttk.Entry(ventana_secundaria)
        entryH3 = ttk.Entry(ventana_secundaria)
        entryH4 = ttk.Entry(ventana_secundaria)
        entryH5 = ttk.Entry(ventana_secundaria)
        
        
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
        entry10.place(y=500, x=100)
        lab10=Label(ventana_secundaria,text=lsPollo[10])
        lab10.place(x=20,y=500)
        entry11.place(y=550, x=100)
        lab11=Label(ventana_secundaria,text=lsPollo[11])
        lab11.place(x=20,y=550)
        entry12.place(y=600, x=100)
        lab12=Label(ventana_secundaria,text=lsPollo[12])
        lab12.place(x=20,y=600)
        entry13.place(y=650, x=100)
        lab13=Label(ventana_secundaria,text=lsPollo[13])
        lab13.place(x=20,y=650)
        entry14.place(y=700, x=100)
        lab14=Label(ventana_secundaria,text=lsPollo[14])
        lab14.place(x=20,y=700)
        entry15.place(y=50, x=400)
        lab15=Label(ventana_secundaria,text=lsPollo[15])
        lab15.place(x=320,y=50)
        
        #posicion y labels huevo
        labH0=Label(ventana_secundaria,text=lsHuevo[0])
        labH0.place(x=420,y=220)
        entryH0.place(y=250, x=400)
        labH1=Label(ventana_secundaria,text=lsHuevo[1])
        labH1.place(x=320,y=250)
        entryH1.place(y=300, x=400)
        labH2=Label(ventana_secundaria,text=lsHuevo[2])
        labH2.place(x=320,y=300)
        entryH2.place(y=350, x=400)
        labH3=Label(ventana_secundaria,text=lsHuevo[3])
        labH3.place(x=320,y=350)
        entryH3.place(y=400, x=400)
        labH4=Label(ventana_secundaria,text=lsHuevo[4])
        labH4.place(x=320,y=400)  
        entryH4.place(y=450, x=400)
        labH5=Label(ventana_secundaria,text=lsHuevo[5])
        labH5.place(x=320,y=450) 
        entryH5.place(y=500, x=400)
        labH6=Label(ventana_secundaria,text=lsHuevo[6])
        labH6.place(x=320,y=500)        
        boton_guardar = ttk.Button(
            ventana_secundaria,
            text="Guardar Precios", 
            command=ventana_secundaria.destroy
        )
        boton_guardar.place(x=600, y=650)
    def ventanaRegistarCompra(self):
        VRC=Toplevel()
        listNombre=["Cliente", "Nro Boleta","Producto","Precio","Kilos","tipo de envase","Aniadir","Borrar","Generar","total"]
        VRC.title("RegistarCompra")
        VRC.geometry("830x500")
        VRC.resizable(0,0)
        ent1=Entry(VRC,width=28)
        ent2=Entry(VRC,width=12)
        ent3=Entry(VRC,width=12)
        ent4=Entry(VRC,width=12)
        ent5=Entry(VRC,width=12)
        list=["hola","como","Estasn"]
        
        tablaitems=ttk.Treeview(VRC,columns=(1,2,3,4))
        tablaitems.column("#0",width=140)
        tablaitems.column(1,width=140, anchor=CENTER)
        tablaitems.column(2,width=140, anchor=CENTER)
        tablaitems.column(3,width=140, anchor=CENTER)
        tablaitems.column(4,width=140, anchor=CENTER)
        
        tablaitems.heading("#0", text=listNombre[2], anchor=CENTER)
        tablaitems.heading(1, text=listNombre[3], anchor=CENTER)
        tablaitems.heading(2, text=listNombre[4], anchor=CENTER)
        tablaitems.heading(3, text=listNombre[5], anchor=CENTER)
        tablaitems.heading(4, text=listNombre[9], anchor=CENTER)
        
        comb1=ttk.Combobox(VRC,state="readonly",values=list,width=20)
        
        bot1=ttk.Button(VRC,text=listNombre[6],command=partial(self.aniadirItem,comb1,ent3,ent4,ent5,tablaitems))
        bot2=ttk.Button(VRC,text=listNombre[7],command=partial(self.eliminarItem,tablaitems))
        bot3=ttk.Button(VRC,text=listNombre[8],command=partial(self.generarBoleta,ent1,ent2,tablaitems))
        
   
        lab1=Label(VRC, text=listNombre[0])
        lab1.place(x=50,y=50)
        ent1.place(x=100,y=50)
        lab2=Label(VRC, text=listNombre[1])
        lab2.place(x=630,y=50)
        ent2.place(x=700,y=50)
        lab3=Label(VRC,text=listNombre[2])
        lab3.place(x=50,y=100)
        
        comb1.place(x=120,y=100)
        
        lab4=Label(VRC, text=listNombre[3])
        lab4.place(x=270,y=100)
        ent3.place(x=320,y=100)
        lab5=Label(VRC, text=listNombre[4])
        lab5.place(x=420,y=100)
        ent4.place(x=460,y=100)
        lab6=Label(VRC, text=listNombre[5])
        lab6.place(x=570,y=100)
        ent5.place(x=670,y=100)
        
        bot1.place(x=50,y=150)
        bot2.place(x=200,y=150)
        bot3.place(x=730,y=450)
        
        tablaitems.place(x=50,y=200)     
        tablaitems.selection   
        
    def aniadirItem(self,combobox,c1,c2,c3,listaElemntos):
        
        precio=float(c1.get())
        itm=combobox.get()
        kilos=float(c2.get())
        descuentoK=float(c3.get())
        total=calcularPresio(pesobruto=kilos,precio=precio,pesoDescontar=descuentoK)

        listaElemntos.insert("",END,text=itm,values=(precio,kilos,descuentoK,total))
    def eliminarItem(self,listItem):
        i=listItem.selection()[0]
        listItem.delete(i)
    def generarBoleta(self,cliente,nroBoleta,listaitems):
        print(cliente.get())
        print(nroBoleta.get())
        lista=[]
        for x in listaitems.get_children():
            elemento=listaitems.item(x)
            lista.append((elemento['text'],elemento["values"]))
        print(lista)
        
l=interfaz()
