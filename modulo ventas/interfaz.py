from functools import partial   
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from baseDeDatos import *
import os,sys
from ventas import *
from datetime import datetime
class interfaz:
    def __init__(self):
        root=Tk()
        self.validarFecha= lambda text:text.isdigit()or "/" in text
        self.validarString= lambda text:text.isalpha()or text==" "
        self.validarNumero= lambda text:text.isdigit()
        self.elementos=[]
        self.lsPollo=["Pollo","P con Menud","P sin Menud","S con Menud","S sin Menud","P. Especial","PiernaMus",
                 "Pecho","Ala","Filete","Rabadilla","Menudo","Higado","Corazon","Hueso de Pecho","Molleja"]
        self.lsHuevo=["Huevo","Primera","Segunda","Tercera","Cuarta","H. Espec","Extra"]
        self.envases=[]
        self.desEnvases=[2,1.5,0]
        root.title("ventas Siloh")
        root.geometry("600x400")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        self.verificarBaseDatos()
        self.FechaHoy()
        
        menuBarra=Menu()
        menuPrecios=Menu(menuBarra,tearoff=False)
        
        menuPrecios.add_command(label="Registar Venta Pollo",accelerator="Ctrl+R",command=self.ventanaRegistarCompraPollo)
        menuPrecios.add_command(label="Registar Venta Huevo",accelerator="Ctrl+H",command=self.ventanaRegistarCompraHuevo)
        menuPrecios.add_command(label="añadir nuevo Envase",accelerator="Ctrl+E",command=self.interfazAniadirEnvace)
        menuPrecios.add_command(label="Cambiar precio",accelerator="Ctrl+P",command=self.ventanaPreciosHoy)
    
        menuBarra.add_cascade(menu=menuPrecios, label="ventas")
        root.config(menu=menuBarra)
        
        root.state('zoomed')
        
        root.mainloop()
        
    def ventanaPreciosHoy(self):
        ventana_secundaria = Toplevel()
        ventana_secundaria.protocol("WM_DELETE_WINDOW", lambda: None)
        ventana_secundaria.title("Ventana secundaria")
        ventana_secundaria.config(width=700, height=700)
        ventana_secundaria.attributes('-topmost',True)
        #ponemos los valores
        
        #parte de crear los valores para pollo 
        
        entry1 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry2 = ttk.Entry(ventana_secundaria,validate='all',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry3 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry4 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry5 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry6 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry7 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry8 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry9 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry10 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry11 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry12 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry13 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry14 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entry15 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"),)
        #entry16 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        
        entryH0 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entryH1 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entryH2 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entryH3 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entryH4 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        entryH5 = ttk.Entry(ventana_secundaria,validate='key',validatecommand=(ventana_secundaria.register(self.es_flotante),"%S"))
        
        
        # Posicionarla en la ventana.
        
        #posicion y labels pollo
        lab0=Label(ventana_secundaria,text=self.lsPollo[0])
        lab0.place(x=120,y=20)
        entry1.place(y=50, x=100)
        lab1=Label(ventana_secundaria,text=self.lsPollo[1])
        lab1.place(x=20,y=50)
        entry2.place(y=100, x=100)
        lab2=Label(ventana_secundaria,text=self.lsPollo[2])
        lab2.place(x=20,y=100)
        entry3.place(y=150, x=100)
        lab3=Label(ventana_secundaria,text=self.lsPollo[3])
        lab3.place(x=20,y=150)
        entry4.place(y=200, x=100)
        lab4=Label(ventana_secundaria,text=self.lsPollo[4])
        lab4.place(x=20,y=200)
        entry5.place(y=250, x=100)
        lab5=Label(ventana_secundaria,text=self.lsPollo[5])
        lab5.place(x=20,y=250)
        entry6.place(y=300, x=100)
        lab6=Label(ventana_secundaria,text=self.lsPollo[6])
        lab6.place(x=20,y=300)
        entry7.place(y=350, x=100)
        lab7=Label(ventana_secundaria,text=self.lsPollo[7])
        lab7.place(x=20,y=350)
        entry8.place(y=400, x=100)
        lab8=Label(ventana_secundaria,text=self.lsPollo[8])
        lab8.place(x=20,y=400)
        entry9.place(y=450, x=100)
        lab9=Label(ventana_secundaria,text=self.lsPollo[9])
        lab9.place(x=20,y=450)
        entry10.place(y=500, x=100)
        lab10=Label(ventana_secundaria,text=self.lsPollo[10])
        lab10.place(x=20,y=500)
        entry11.place(y=550, x=100)
        lab11=Label(ventana_secundaria,text=self.lsPollo[11])
        lab11.place(x=20,y=550)
        entry12.place(y=600, x=100)
        lab12=Label(ventana_secundaria,text=self.lsPollo[12])
        lab12.place(x=20,y=600)
        entry13.place(y=650, x=100)
        lab13=Label(ventana_secundaria,text=self.lsPollo[13])
        lab13.place(x=20,y=650)
        entry14.place(y=50, x=400)
        lab14=Label(ventana_secundaria,text=self.lsPollo[14])
        lab14.place(x=300,y=50)
        entry15.place(y=100, x=400)
        lab15=Label(ventana_secundaria,text=self.lsPollo[15])
        lab15.place(x=300,y=100)
        
        #posicion y labels huevo
        labH0=Label(ventana_secundaria,text=self.lsHuevo[0])
        labH0.place(x=420,y=220)
        entryH0.place(y=250, x=400)
        labH1=Label(ventana_secundaria,text=self.lsHuevo[1])
        labH1.place(x=300,y=250)
        entryH1.place(y=300, x=400)
        labH2=Label(ventana_secundaria,text=self.lsHuevo[2])
        labH2.place(x=300,y=300)
        entryH2.place(y=350, x=400)
        labH3=Label(ventana_secundaria,text=self.lsHuevo[3])
        labH3.place(x=300,y=350)
        entryH3.place(y=400, x=400)
        labH4=Label(ventana_secundaria,text=self.lsHuevo[4])
        labH4.place(x=300,y=400)  
        entryH4.place(y=450, x=400)
        labH5=Label(ventana_secundaria,text=self.lsHuevo[5])
        labH5.place(x=300,y=450) 
        entryH5.place(y=500, x=400)
        labH6=Label(ventana_secundaria,text=self.lsHuevo[6])
        labH6.place(x=300,y=500)        
        self.cargarValoresPrecio(entry1,entry2,entry3,entry4,entry5,entry6,
                            entry7,entry8,entry9,entry10,entry11,entry12,entry13,entry14,entry15,
                            entryH0,entryH1,entryH2,entryH3,entryH4,entryH5)
        
        boton_guardar = ttk.Button(
            ventana_secundaria,
            text="Guardar Precios", 
            command=partial(self.salirGuardar,ventana_secundaria,entry1,entry2,entry3,entry4,entry5,entry6,
                            entry7,entry8,entry9,entry10,entry11,entry12,entry13,entry14,entry15,
                            entryH0,entryH1,entryH2,entryH3,entryH4,entryH5)
        )
        boton_guardar.place(x=600, y=650)
        
    def ventanaRegistarCompraPollo(self):
        
        VRC=Toplevel()
        listNombre=["Cliente","Fecha","Nro Boleta","Producto","Precio","Kilos","tipo de envase","cant","total","Aniadir","Borrar","Generar"]
        VRC.title("RegistarCompraPollo")
        VRC.geometry("830x500")
        VRC.resizable(0,0)
        ent0=Entry(VRC,width=28,validate='key',validatecommand=(VRC.register(self.validarString),"%S"))
        ent1=Entry(VRC,width=12,validate='key',validatecommand=(VRC.register(self.validarFecha),"%S"))
        ent2=Entry(VRC,width=12,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent3=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent4=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent5=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.validarNumero),"%S"))
        
        ent1.bind('<Key>',partial(self.ayudaFecha,ent1))
        ent1.bind("<BackSpace>",lambda _: ent1.delete(END))
        lista=devolverListaDeItemNombre([self.lsPollo[0]])
        
        self.envases=devolverListaDeItemNombre(["envase"])
        self.desEnvases=devolverListaDeItemPrecio(["envase"])
        self.elementos=devolverListaDeItemPrecio([self.lsPollo[0]])
        
        tablaitems=ttk.Treeview(VRC,columns=(1,2,3,4))
        tablaitems.column("#0",width=140)
        tablaitems.column(1,width=140, anchor=CENTER)
        tablaitems.column(2,width=140, anchor=CENTER)
        tablaitems.column(3,width=140, anchor=CENTER)
        tablaitems.column(4,width=140, anchor=CENTER)
        
        tablaitems.heading("#0", text=listNombre[3], anchor=CENTER)
        tablaitems.heading(1, text=listNombre[4], anchor=CENTER)
        tablaitems.heading(2, text=listNombre[5]+" B", anchor=CENTER)
        tablaitems.heading(3, text=listNombre[5]+" N", anchor=CENTER)
        tablaitems.heading(4, text=listNombre[8], anchor=CENTER)
        
        comb1=ttk.Combobox(VRC,state="readonly",values=lista,width=20)
        comb2=ttk.Combobox(VRC,state="readonly",values=self.envases,width=12)
        comb1.bind('<<ComboboxSelected>>',partial(self.cambiarValor,ent3,comb1))
        bot1=ttk.Button(VRC,width=50,text=listNombre[9],command=partial(self.aniadirItemP,comb1,ent3,ent4,ent5,comb2,tablaitems))
        bot2=ttk.Button(VRC,width=50,text=listNombre[10],command=partial(self.eliminarItem,tablaitems))
        bot3=ttk.Button(VRC,text=listNombre[11],command=partial(self.generarBoleta,VRC,ent0,ent1,ent2,tablaitems))
        
   
        lab0=Label(VRC, text=listNombre[0])
        lab0.place(x=50,y=50)
        ent0.place(x=100,y=50)
        lab1=Label(VRC, text=listNombre[1])
        lab1.place(x=450,y=50)
        ent1.place(x=500,y=50)
        lab2=Label(VRC, text=listNombre[2])
        lab2.place(x=630,y=50)
        ent2.place(x=700,y=50)
        lab3=Label(VRC,text=listNombre[3])
        lab3.place(x=50,y=100)
        
        comb1.place(x=120,y=100)
        
        lab4=Label(VRC, text=listNombre[4])
        lab4.place(x=270,y=100)
        ent3.place(x=315,y=100)
        lab5=Label(VRC, text=listNombre[5])
        lab5.place(x=370,y=100)
        ent4.place(x=415,y=100)
        lab6=Label(VRC, text=listNombre[6])
        lab6.place(x=480,y=100)
        comb2.place(x=580,y=100)
        lab7=Label(VRC, text=listNombre[7])
        lab7.place(x=680,y=100)
        ent5.place(x=720,y=100)
        
        bot1.place(x=50,y=150)
        bot2.place(x=440,y=150)
        bot3.place(x=730,y=450)
        
        tablaitems.place(x=50,y=200)
        
        ent1.insert(0,self.FechaHoy())
        
    def interfazAniadirEnvace(self):
        IAE=Toplevel()
        IAE.geometry("400x200")
        ListaTex=["Nombre Envase","Peso en KiloGramo (0.0)"]
        L1=Label(IAE,text=ListaTex[0]) 
        L2=Label(IAE,text=ListaTex[1])
        verficarNumeAlfa= lambda texts:texts.isdigit() or texts.isalpha()
        E1=Entry(IAE,validate='key',validatecommand=(IAE.register(verficarNumeAlfa),"%S"))
        L1.place(x=20,y=50)
        E1.place(x=150,y=50) 
        
        E2=Entry(IAE,validate='key',validatecommand=(IAE.register(self.es_flotante),"%S"))
        L2.place(x=20,y=100)
        E2.place(x=150,y=100)
        
        b1=ttk.Button(IAE,text="agregar",command=partial(self.aniadirEnvace,IAE,E1,E2))
        b1.place(x=300,y=150)
        
    def ventanaRegistarCompraHuevo(self):
        
        VRC=Toplevel()
        listNombre=["Cliente","Fecha","Nro Boleta","Producto","Precio","cant","tipo de envase","cant","total","Aniadir","Borrar","Generar"]
        VRC.title("RegistarCompraHuevo")
        VRC.geometry("830x500")
        VRC.resizable(0,0)
        ent0=Entry(VRC,width=28,validate='key',validatecommand=(VRC.register(self.validarString),"%S"))
        ent1=Entry(VRC,width=12,validate='key',validatecommand=(VRC.register(self.validarFecha),"%S"))
        ent2=Entry(VRC,width=12,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent3=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent4=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.es_flotante),"%S"))
        ent5=Entry(VRC,width=8,validate='key',validatecommand=(VRC.register(self.validarString),"%S"))
        
        ent1.bind('<Key>',partial(self.ayudaFecha,ent1))
        ent1.bind("<BackSpace>",lambda _: ent1.delete(END))
        lista=devolverListaDeItemNombre([self.lsHuevo[0]])
        
        self.envases=devolverListaDeItemNombre(["envase"])
        self.desEnvases=devolverListaDeItemPrecio(["envase"])
        self.elementos=devolverListaDeItemPrecio([self.lsHuevo[0]])
        
        tablaitems=ttk.Treeview(VRC,columns=(1,2,3))
        tablaitems.column("#0",width=175)
        tablaitems.column(1,width=175, anchor=CENTER)
        tablaitems.column(2,width=175, anchor=CENTER)
        tablaitems.column(3,width=175, anchor=CENTER)
        
        
        tablaitems.heading("#0", text=listNombre[3], anchor=CENTER)
        tablaitems.heading(1, text=listNombre[4], anchor=CENTER)
        tablaitems.heading(2, text=listNombre[7]+"idad", anchor=CENTER)
        tablaitems.heading(3, text=listNombre[8], anchor=CENTER)
        
        comb1=ttk.Combobox(VRC,state="readonly",values=lista,width=20)
        comb2=ttk.Combobox(VRC,state="readonly",values=self.envases,width=12)
        comb1.bind('<<ComboboxSelected>>',partial(self.cambiarValor,ent3,comb1))
        bot1=ttk.Button(VRC,width=50,text=listNombre[9],command=partial(self.aniadirItemH,comb1,ent3,ent4,tablaitems))
        bot2=ttk.Button(VRC,width=50,text=listNombre[10],command=partial(self.eliminarItem,tablaitems))
        bot3=ttk.Button(VRC,text=listNombre[11],command=partial(self.generarBoleta,VRC,ent0,ent1,ent2,tablaitems))
        
   
        lab0=Label(VRC, text=listNombre[0])
        lab0.place(x=50,y=50)
        ent0.place(x=100,y=50)
        lab1=Label(VRC, text=listNombre[1])
        lab1.place(x=450,y=50)
        ent1.place(x=500,y=50)
        lab2=Label(VRC, text=listNombre[2])
        lab2.place(x=630,y=50)
        ent2.place(x=700,y=50)
        lab3=Label(VRC,text=listNombre[3])
        lab3.place(x=50,y=100)
        
        comb1.place(x=120,y=100)
        
        lab4=Label(VRC, text=listNombre[4])
        lab4.place(x=270,y=100)
        ent3.place(x=315,y=100)
        lab5=Label(VRC, text=listNombre[5])
        lab5.place(x=370,y=100)
        ent4.place(x=415,y=100)
        lab6=Label(VRC, text=listNombre[6])
        lab6.place(x=480,y=100)
        ent5.place(x=580,y=100)
        ent5.insert(0,"maple")
        
        
        bot1.place(x=50,y=150)
        bot2.place(x=440,y=150)
        bot3.place(x=730,y=450)
        
        tablaitems.place(x=50,y=200)
        
        ent1.insert(0,self.FechaHoy())
        
    
                   
    def verificarBaseDatos(self):
        if not(os.path.exists("./silohDataBase.db")):
            
            vl=messagebox.askyesno(message="No se detecto './silohDataBase.db', desea crear el archivo (SI), en caso contrario se cerrara hasta que se encuntre el archivo (NO) ")
            if vl:
                crearBaseDeDatos()
            else:
                sys.exit()
    
    def aniadirEnvace(self,v1,e1,e2):
        tex1=e1.get()
        tex2=float(e2.get())
        anadirtablaArticulo("envase",tex1,tex2)
        v1.destroy()
        
        
    def aniadirItemP(self,combobox,c1,c2,c3,combobox2,listaElemntos):
        
        precio=float(c1.get())
        itm=combobox.get()
        kilosB=float(c2.get())
        kilosDes=calcularDescuento(float(self.desEnvases[combobox2.current()]),int(c3.get()))
        pesoNeto=calcularNeto(kilosB,kilosDes)
        total=calcularPrecio(pesoNeto=pesoNeto,precio=precio)

        listaElemntos.insert("",END,text=itm,values=(precio,kilosB,pesoNeto,total))
      
    def aniadirItemH(self,combobox,c1,c2,listaElemntos):
        precio=float(c1.get())
        itm=combobox.get()
        cantidad=float(c2.get())
        total=calcularPrecio(pesoNeto=cantidad,precio=precio)

        listaElemntos.insert("",END,text=itm,values=(precio,cantidad,total))
        
    def eliminarItem(self,listItem):
        i=listItem.selection()[0]
        listItem.delete(i)
        
    def generarBoleta(self,ventana,cliente,fecha,nroBoleta,listaitems):
        c=cliente.get()
        f=str(fecha.get()).replace("/","-")
        nb=nroBoleta.get()
        for x in listaitems.get_children():
            elemento=listaitems.item(x)
            producto=elemento['text']
            items=list(elemento["values"])
            if len(items)==3: 
                res=items[:1]
                res+=[items[1]]
                res+=items[1:]
            else:
                res=items
            agregarVenta(cliente=c,fecha=f,numeroBolete=nb,producto=producto,precio=res[0],cantBruto=res[1],cantNeto=res[2],total=res[3])
        
        ventana.destroy()    
        
        
    def cambiarValor(self,o,a,v):
        o.delete(0,END)
        vla=a.current()
        o.insert('0',self.elementos[vla])
        
    def es_flotante(self,variable):
        try:
            
            float(variable)
            return True
        except:
            if(variable=='.'):return True
            return False
    def salirGuardar(self,v,entry1,entry2,entry3,entry4,entry5,entry6,
                            entry7,entry8,entry9,entry10,entry11,entry12,entry13,entry14,entry15,
                            entryH0,entryH1,entryH2,entryH3,entryH4,entryH5):
        modificarArticulo(self.lsPollo[1],entry1.get())
        modificarArticulo(self.lsPollo[2],entry2.get())
        modificarArticulo(self.lsPollo[3],entry3.get())
        modificarArticulo(self.lsPollo[4],entry4.get())
        modificarArticulo(self.lsPollo[5],entry5.get())
        modificarArticulo(self.lsPollo[6],entry6.get())
        modificarArticulo(self.lsPollo[7],entry7.get())
        modificarArticulo(self.lsPollo[8],entry8.get())
        modificarArticulo(self.lsPollo[9],entry9.get())
        modificarArticulo(self.lsPollo[10],entry10.get())
        modificarArticulo(self.lsPollo[11],entry11.get())
        modificarArticulo(self.lsPollo[12],entry12.get())
        modificarArticulo(self.lsPollo[13],entry13.get())
        modificarArticulo(self.lsPollo[14],entry14.get())
        modificarArticulo(self.lsPollo[15],entry15.get())
        
        modificarArticulo(self.lsHuevo[1],entryH0.get())
        modificarArticulo(self.lsHuevo[2],entryH1.get())
        modificarArticulo(self.lsHuevo[3],entryH2.get())
        modificarArticulo(self.lsHuevo[4],entryH3.get())
        modificarArticulo(self.lsHuevo[5],entryH4.get())
        modificarArticulo(self.lsHuevo[6],entryH5.get())
        
        self.elementos=devolverListaDeItemPrecio([self.lsPollo[0],self.lsHuevo[0]])
        
        
        v.destroy()
    def FechaHoy(self):
        now=datetime.now().date()
        now=str(now).split("-")
        now=now[::-1]
        return "/".join(now)
        
    def ayudaFecha(self,ent,event):
        if event.char.isdigit():
           texto=ent.get()
           letras=0
           for i in texto:
               letras+=1
           if letras==2:
               ent.insert(2,"/")
           elif letras==5:
               ent.insert(5,"/")
        else:
            return "break"
    
    def cargarValoresPrecio(self,entry1,entry2,entry3,entry4,entry5,entry6,
                            entry7,entry8,entry9,entry10,entry11,entry12,entry13,entry14,entry15,
                            entryH0,entryH1,entryH2,entryH3,entryH4,entryH5):
        listaPrecio=devolverListaDeItemPrecio([self.lsPollo[0],self.lsHuevo[0]])
        entry1.insert(0,listaPrecio[0])
        entry2.insert(0,listaPrecio[1])
        entry3.insert(0,listaPrecio[2])
        entry4.insert(0,listaPrecio[3])
        entry5.insert(0,listaPrecio[4])
        entry6.insert(0,listaPrecio[5])
        entry7.insert(0,listaPrecio[6])
        entry8.insert(0,listaPrecio[7])
        entry9.insert(0,listaPrecio[8])
        entry10.insert(0,listaPrecio[9])
        entry11.insert(0,listaPrecio[10])
        entry12.insert(0,listaPrecio[11])
        entry13.insert(0,listaPrecio[12])
        entry14.insert(0,listaPrecio[13])
        entry15.insert(0,listaPrecio[14])
        entryH0.insert(0,listaPrecio[15])
        entryH1.insert(0,listaPrecio[16])
        entryH2.insert(0,listaPrecio[17])
        entryH3.insert(0,listaPrecio[18])
        entryH4.insert(0,listaPrecio[19])
        entryH5.insert(0,listaPrecio[20])
        
l=interfaz()
