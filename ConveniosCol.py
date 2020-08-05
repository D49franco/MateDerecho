import pandas as pd
import numpy as np
from IPython.core.display import HTML, display
import ipywidgets as widgets
from ipywidgets import interact, interactive, Layout


display(HTML("<H1>@ConveniosCol:</H1><br><p>El siguiente aplicativo muestra los convenios que tiene determinado establecimiento. Puedes buscar por convenio o por establecimiento.</p>"))
display(HTML("Hecho por David Andrés Franco Quintero"))

df=pd.DataFrame(pd.read_excel("matriz_fidela.xlsx"))
establecimientos=list(df["ESTABLECIMIENTOS"])
convenios=list(df.columns)
convenios.remove("ESTABLECIMIENTOS")

def buscador(establecimiento, convenio):
    establecimiento=str(establecimiento)
    convenio=str(convenio)
    pd.set_option('display.max_rows',1000) 
    
        
    fila=df[df["ESTABLECIMIENTOS"]==establecimiento]  ## así hago que busque "ADVENIO" en "ESTABLECIMIENTOS" y me muestra la fila indicada
    display(fila)
    columna=df[["ESTABLECIMIENTOS",convenio]] ##muestra las dos columnas pedidas
    display(columna)

    


style = {'description_width': 'initial',}
l = Layout( height='auto', width='600px')
wide=widgets.Select(options=establecimientos,description="Elige un establecimiento",style=style,layout=l)
widc=widgets.Select(options=convenios,description="Elige un convenio",style=style,layout=l)
interact(buscador,establecimiento=wide,convenio=widc)




#buscador("ADVENIO","COMPENSAR")
