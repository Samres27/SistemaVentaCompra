import sqlite3
def crearBaseDeDatos():
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #crear tablas
        #tabla articulo con 3 id,categorias (pollo,huevo, envace),valor
        conectar.execute("""CREATE TABLE IF NOT EXISTS articulo(id integer primary key autoincrement,tipo text,nombre text,valor float)
                         """) 
        #crear venta id,cliente,fecha,nroBoleta,producto,precio,cantBruto,cantNeto,total
        conectar.execute("""CREATE TABLE IF NOT EXISTS  venta(id integer primary key autoincrement,cliente text,fecha Date,nroBoleta Int,
                         producto text,precio Float,cantBruto Float,cantNeto Float,total Float)""") 
        lsPollo=["Pollo","P con Menudo","P sin Menudo","S con Menudo","S sin Menudo","P. Especial","PiernaMuslo",
                 "Pecho","Ala","Filete","Rabadilla","Menudo","Higado","Corazon","Hueso de Pecho","Molleja"]
        
        anadirtablaArticulo("Pollo",lsPollo[1],0.0)
        anadirtablaArticulo("Pollo",lsPollo[2],0.0)
        anadirtablaArticulo("Pollo",lsPollo[3],0.0)
        anadirtablaArticulo("Pollo",lsPollo[4],0.0)
        anadirtablaArticulo("Pollo",lsPollo[5],0.0)
        anadirtablaArticulo("Pollo",lsPollo[6],0.0)
        anadirtablaArticulo("Pollo",lsPollo[7],0.0)
        anadirtablaArticulo("Pollo",lsPollo[8],0.0)
        anadirtablaArticulo("Pollo",lsPollo[9],0.0)
        anadirtablaArticulo("Pollo",lsPollo[10],0.0)
        anadirtablaArticulo("Pollo",lsPollo[11],0.0)
        anadirtablaArticulo("Pollo",lsPollo[12],0.0)
        anadirtablaArticulo("Pollo",lsPollo[13],0.0)
        anadirtablaArticulo("Pollo",lsPollo[14],0.0)
        anadirtablaArticulo("Pollo",lsPollo[15],0.0)
        
        lsHuevo=["Huevo","Primera","Segunda","Tercera","Cuarta","H. Espec","Extra"]
        
        anadirtablaArticulo("Huevo",lsHuevo[1],0.0)
        anadirtablaArticulo("Huevo",lsHuevo[2],0.0)
        anadirtablaArticulo("Huevo",lsHuevo[3],0.0)
        anadirtablaArticulo("Huevo",lsHuevo[4],0.0)
        anadirtablaArticulo("Huevo",lsHuevo[5],0.0)
        anadirtablaArticulo("Huevo",lsHuevo[6],0.0)
        
        conectar.close()
    except Error as e:
        print(e)
    
def obtenerDatosTipo(tipo):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #obtener los valores del tipo
        vl=conectar.execute("""select id,tipo,nombre,valor from articulo where tipo='%s'
                         """%(tipo)) 
        valores=[]
        for x in vl:
            valores.append(x)
        conectar.close()
        return valores
    except Error as e:
        print(e)
def obtenerVentaNombre(cliente):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #obtener los valores del tipo
        vl=conectar.execute("""select id,cliente,fecha,nroBoleta,producto,precio,cantBruto,cantNeto,total from venta where cliente='%s'
                         """%(cliente)) 
        valores=[]
        for x in vl:
            valores.append(x)
        conectar.close()
        return valores
    except Error as e:
        print(e)
def obtenerVentaNombreFecha(cliente,fecha):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #obtener los valores del tipo
        vl=conectar.execute("""select id,cliente,fecha,nroBoleta,producto,precio,cantBruto,cantNeto,total from venta where cliente='%s' and fecha='%s'
                         """%(cliente,fecha)) 
        valores=[]
        for x in vl:
            valores.append(x)
        conectar.close()
        return valores
    except Error as e:
        print(e)
def obtenerListaCliente():
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #obtener los valores del tipo
        vl=conectar.execute("""SELECT DISTINCT cliente from venta 
                         """) 
        valores=[]
        for x in vl:
            (a)=x
            valores.append(a[0])
        conectar.close()
        return valores
    except Error as e:
        print(e)
        
def anadirtablaArticulo(tipo,nombre,valor):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #anadimos el articulo que con los ultimos 3 ya que el el primero es la key
        conectar.execute("insert into articulo(tipo,nombre,valor) values (?,?,?)",(tipo,nombre,valor)) 
        conectar.commit()
        conectar.close()
    except Error as e:
        print(e)
        
def devolverListaDeItemPrecio(listas):
    tabl="articulo"
    respuestap=[]
    respuestat=[]
    for x in listas:
        respuestap+=obtenerDatosTipo(tipo=x)
    
    for x in respuestap:
        i,t,n,v=x
        respuestat.append(v)
    return respuestat

def modificarArticulo(nombre,valorCambiar):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #modificar un articulo que se coincida con el nombre 
        conectar.execute("update articulo set valor=? where nombre=?",(valorCambiar,nombre)) 
        conectar.commit()
        conectar.close()
    except Error as e:
        print(e)

def devolverListaDeItemPrecio(listas):
    tabl="articulo"
    respuestap=[]
    respuestat=[]
    for x in listas:
        respuestap+=obtenerDatosTipo(tipo=x)
    
    for x in respuestap:
        i,t,n,v=x
        respuestat.append(v)
    return respuestat
def devolverListaDeItemNombre(lista):
    tabl="articulo"
    respuestap=[]
    respuestat=[]
    for x in lista:
        respuestap+=obtenerDatosTipo(tipo=x)
    
    for x in respuestap:
        i,t,n,v=x
        respuestat.append(n)
    return respuestat
def agregarVenta(cliente,fecha,numeroBolete,producto,precio,cantBruto,cantNeto,total):
    conectar=sqlite3.connect("./silohDataBase.db")
    try:
        #anadimos el articulo que con los ultimos 3 ya que el el primero es la key
        conectar.execute("insert into venta(cliente,fecha,nroBoleta,producto,precio,cantBruto,cantNeto,total) values (?,?,?,?,?,?,?,?)",(cliente,fecha,numeroBolete,producto,precio,cantBruto,cantNeto,total)) 
        conectar.commit()
        conectar.close()
    except Error as e:
        print(e)
        
        

