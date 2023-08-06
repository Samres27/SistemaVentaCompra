import jinja2
import pdfkit
from datetime import datetime
from baseDeDatos import *
from ventas import *
def crearPDFTemplate(nombreCliente,cantidadTotal,listaElementos):
    today_date = datetime.today().strftime("%d %b, %Y")
    tablaV=valoresTabla(listaVentas=listaElementos)
    

    context = {'nombreCliente': nombreCliente, 'fechaImpresion': today_date, 'cantidadTotal': cantidadTotal,
            "contenidoExtraTabla":tablaV
            }
    template_loader = jinja2.FileSystemLoader(".\\ArchivosNecesario\\")
    template_env = jinja2.Environment(loader=template_loader)

    html_template = "./ej2.html"
    template = template_env.get_template(html_template)
    output_text = template.render(context)
    config = pdfkit.configuration(wkhtmltopdf='./ArchivosNecesario/wkhtmltopdf/bin/wkhtmltopdf.exe')
    output_pdf = './ArchivosNecesario/ej2.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='./ArchivosNecesario/ej2.css')

def crearPDFventas(cliente):
    listaVentas=obtenerVentaNombre(cliente=cliente)
    total=calcularListaTotal(listaElmentos=listaVentas)
    crearPDFTemplate(nombreCliente=cliente,cantidadTotal=total,listaElementos=listaVentas)

def valoresTabla(listaVentas):
    valorTabla=""
    for x in listaVentas:
        id,cliente,fecha,nroBoleta,producto,precio,cantBruto,cantNeto,total=x
        valorTabla+= """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>"""%(producto,fecha,cantNeto,precio,total)
    return valorTabla


crearPDFventas("samuel")