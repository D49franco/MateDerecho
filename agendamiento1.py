from PIL import Image
import ipywidgets as widgets
from ipywidgets import interact, interactive, Layout
from IPython.core.display import HTML, display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

display(HTML(' <div style="background-color: #023324; "><p>'+
                         '<br></p>     <img src="https://www.uexternado.edu.co/wp-content/themes/externado_theme/images/logo-uec.svg" alt="Universidad Externado" width="150" align="left">  '+
                         '<h1  style="color: white;font-family:Lucida Sans Unicode, Lucida Grande, sans-serif" align="center">Horarios Pitágoras - Matemáticas para Derecho</h1> '+
                         '<p><br></p></div>'))

   
display(HTML("A continuación se encuentran los horarios de asesoría de Pitágoras:"))
im = Image.open('horario_fermat.png','r')
display(im)
print()
display(HTML("Aquí puedes elegir a un profesor, y obtendrás información sobre su asesoría:"))

asesoria={"ANTONIO PAZ":"Correo: antonio.paz@uexternado.edu.co ID: 964 8369 2975 Contraseña: 181480","EMMA CAMARGO":"Correo: emma.camargo@uexternado.edu.co Enlace: https://uexternado.zoom.us/j/205513673 Contraseña: Asesoría1","SEBASTIÁN BALLÉN":"Correo: juan.ballen@uexternado.edu.co ID: 988 4995 2447 Contraseña: Mate_Dere.","LILIANA TORRES":"Correo: lilianac.torres@uexternado.edu.co ID: 994 9243 1994 Contraseña: 132082 ","JULIÁN ROBLEDO (MARTES)":"Correo: julian.robledo@uexternado.edu.co Enlace: https://uexternado.zoom.us/j/97724853691","CAMILA MERCHÁN (MIÉRCOLES)":"Correo: camila.merchan@uexternado.edu.co ID: 957 8812 0214 Contraseña: 28202021","DAVID DÍAZ":"Correo: david.diaz@uexternado.edu.co ID: 991 1593 6286 Contraseña: 1123581321","DAVID FRANCO":"Correo: david.franco@uexternado.edu.co ID: 991 8821 5909 Contraseña: Sherlock1!","JULIÁN ROBLEDO (VIERNES)":"Correo: julian.robledo@uexternado.edu.co Enlace: https://uexternado.zoom.us/j/91439045255","CAMILA MERCHÁN (VIERNES)":"Correo: camila.merchan@uexternado.edu.co ID: 989 7959 6738  Contraseña: 20202021 ", "CAMILO DE LA CRUZ":"Correo: camilo.delacruz@uexternado.edu.co"}
claves=list(asesoria.keys())
def funcion(opcion):
    
    display(HTML((asesoria[opcion])))
    if opcion=="CAMILO DE LA CRUZ":
        display(HTML("Para tener una asesoría con el profesor Camilo, escríbele un correo manifestando tu intención. Él agendará contigo una asesoría."))
    else:
        display(HTML("Envíale un correo al profesor informándole en que fecha y hora irás, y sobre cuál tema tienes dudas."))

style = {'description_width': 'initial',}
l = Layout( height='auto', width='400px')
wid=widgets.Select(options=claves,description="Elige un profesor",style=style,layout=l)
interact(funcion,opcion=wid)
def llamafuncion():
    interact(funcion,opcion=wid)
    return