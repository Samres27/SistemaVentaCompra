from tkinter import *

from tkinter import ttk
def item_selected(event):
    for selected_item in tv.selection():
        print (selected_item)

ventana = Tk()
ventana.title('Ejemplo de TreeView')
ventana.geometry('400x300')
ventana['bg']='#fb0'

tv = ttk.Treeview(ventana, columns=("c1","c2","c3"))

tv.column("#0",width=80)
tv.column("col1",width=80, anchor=CENTER)
tv.column("col2",width=80, anchor=CENTER)

tv.heading("#0", text="Producto", anchor=CENTER)
tv.heading("col1", text="Precio", anchor=CENTER)
tv.heading("col2", text="Cantidad", anchor=CENTER)

tv.insert("",END,text="Azucar", values=("28","2"))
tv.insert("",END,text="Refresco", values=("16","3"))
tv.insert("",END,text="AQceite", values=("34","1"))
tv.pack()



ventana.mainloop()