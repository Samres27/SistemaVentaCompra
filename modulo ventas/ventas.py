
def calcularPrecio(pesoNeto,precio):
    return (pesoNeto)*precio

def calcularNeto(precioBruto,descontar):
    return precioBruto-descontar

def calcularDescuento(descuentoUnitario,cantE):
    return descuentoUnitario*cantE

def calcularListaTotal(listaElmentos):
    cantidad=0
    for x in listaElmentos:
        _,_,_,_,_,_,_,_,v=x
        cantidad+=float(v)
    return cantidad