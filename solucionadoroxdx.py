#Se requiere un programa que dé la opción si ingresar precio y cantidad o ingresar la ecuación, resuelva y halle las cantidades y el precio de equilibrio. El programa mostrará la gráfica y dirá las zonas de abundancia y escasez.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from sympy import *
from sympy import init_printing
init_printing()
import ipywidgets as widgets
from ipywidgets import interact, interactive, Layout
import csv
from turtle import *
from IPython.core.display import HTML, display
init_printing(use_latex=True)


#%precision 2

display(HTML(' <div style="background-color: #023324; "><p>'+
             '<br></p>     <img src="https://www.uexternado.edu.co/wp-content/themes/externado_theme/images/logo-uec.svg" alt="Universidad Externado" width="150" align="left">  '+
             '<h1  style="color: white;font-family:Lucida Sans Unicode, Lucida Grande, sans-serif" align="center">Solucionador de punto de equilibrio en Oferta y Demanda</h1> '+
             '<p><br></p></div>'))
display(HTML("Ingrese los siguientes valores para efectuar la solución:"))

def graficador(preciodx1,qdx1,preciodx2,qdx2,precioox1,qox1,precioox2,qox2):
    
    
    
    
    
    
    

    
    
    try:
        
        pendiented=(qdx2-qdx1)/(preciodx2-preciodx1)
        pendienteo=(qox2-qox1)/(precioox2-precioox1)
        p=sp.symbols("p")
        Dx=sp.symbols("Dx=")
        Ox=sp.symbols("Ox=")
        complementod=(pendiented*-preciodx1)+qdx1
        complementoo=(pendienteo*-precioox1)+qox1


        sp.eqox=pendienteo*p+complementoo
        sp.eqdx=pendiented*p+complementod
        sp.Dx=Dx
        sp.Ox=Ox

        fo=str(pendienteo)+"*xx+"+str(complementoo)
        fd=str(pendiented)+"*xx+"+str(complementod)

        xmaximo=-complementod/pendiented
        xx=np.linspace(0,xmaximo,100)
        yyd=eval(fd)
        yyo=eval(fo)



        x,y=symbols('x y')
        equi=list(linsolve([x*pendiented+complementod-y,x*pendienteo+complementoo-y],(x,y)))
        equi=equi[0]
        sp.equi=equi
        if equi[0]==int(equi[0]):
            sp.precioequi= int(equi[0])
        else:
            sp.precioequi=equi[0]
        if equi[1]==int(equi[1]):
            sp.cantidadequi=int(equi[1])
        else:
            sp.cantidadequi=equi[1]






        
        display(HTML('Para un precio de ${}$ las unidades demandadas fueron ${}$; para un precio de ${}$ las unidades demandadas fueron ${}$. La ecuación de demanda es:'.format(preciodx1,qdx1,preciodx2,qdx2)))
        print()
        display(HTML("$D_x={}$".format(latex(sp.eqdx))))             
        print()
        display(HTML('Para un precio de ${}$ las unidades ofertadas fueron ${}$; para un precio de ${}$ las unidades ofertadas fueron ${}$. La ecuación de oferta es:'.format(precioox1,qox1,precioox2,qox2)))
        print()
        display(HTML("$O_x={}$".format(latex(sp.eqox))))
        print()
        display(HTML('El punto de equilibrio es ${}$. Esto quiere decir que a un precio de ${}$, las cantidades ofertadas y demandas son las mismas (${}$).'.format(sp.equi,sp.precioequi,sp.cantidadequi)))
        print()
        display(HTML('Con un precio superior a ${}$, las cantidades ofertadas superan a las cantidades demandadas (abundancia o sobreoferta). Con un precio inferior a ${}$ las cantidades demandadas superan a las cantidades ofertadas (escasez o sobredemanda).'.format(sp.precioequi,sp.precioequi)))




        ordenacion=[[preciodx1,qdx1],[preciodx2,qdx2],[precioox1,qox1],[precioox2,qox2]]
        maxpreciod=max(ordenacion[0][0],ordenacion[1][0])
        maxprecioo=max(ordenacion[2][0],ordenacion[3][0])
        maxqd=max(ordenacion[0][1],ordenacion[1][1])
        maxqo=max(ordenacion[1][1],ordenacion[3][1])
        minqd=min(ordenacion[0][1],ordenacion[1][1])
        minqo=min(ordenacion[1][1],ordenacion[3][1])

        dicci={qdx1:preciodx1,qdx2:preciodx2,qox1:precioox1,qox2:precioox2}








        fig=plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(yyd,xx,color='blue', linewidth=3, label="{}{}".format(sp.Dx,sp.eqdx))
        ax.plot(yyo,xx, color='orange', linewidth=3, label="{}{}".format(sp.Ox,sp.eqox))
        ax.plot(equi[1],equi[0], "ro",label="Equilibrio={}".format(sp.equi))
        ax.set_xlabel('Cantidades')
        ax.set_ylabel('Precio')
        ax.set_title("Gráfico de Oferta y Demanda") 
        ax.legend()
        maxx=max(qdx1,qdx2,qox1,qox2)
        maxy=max(preciodx1,preciodx2,precioox1,precioox2)


        plt.xlim(0,maxx+20)
        plt.ylim(0,maxy+20)

        #abundancia=plt.plot([cantidadequi,maxqo,minqd,cantidadequi],[precioequi,dicci[maxqo],dicci[minqd],precioequi], linewidth=1,color="red")  


        plt.show()
        
        
        
    except: 
        display(HTML("Ingrese valores adecuados, de tal manera que los precios de la demanda no sean los mismos. Igual para los precios de la oferta."))                       
    
    
    
style = {'description_width': 'initial',}
l = Layout( height='auto', width='400px')
widpreciodx1=widgets.FloatText(description="Primer precio de demanda",style=style,layout=l)
widpreciodx2=widgets.FloatText(description="Segundo precio de demanda",style=style,layout=l)
widprecioox1=widgets.FloatText(description="Primer precio de oferta",style=style,layout=l)
widprecioox2=widgets.FloatText(description="Segundo precio de oferta",style=style,layout=l)
widqdx1=widgets.FloatText(description="Primer valor de cantidades demandadas",style=style,layout=l)
widqdx2=widgets.FloatText(description="Segundo valor de cantidades demandadas",style=style,layout=l)
widqox1=widgets.FloatText(description="Primer valor de cantidades ofertadas",style=style,layout=l)
widqox2=widgets.FloatText(description="Segundo valor de cantidades ofertadas",style=style,layout=l)



def llamafuncion():
    interact(graficador,preciodx1=widpreciodx1,qdx1=widqdx1,preciodx2=widpreciodx2,qdx2=widqdx2,precioox1=widprecioox1,qox1=widqox1,precioox2=widprecioox2,qox2=widqox2) 
    return
#graficador(12,20,28,12,12,8,28,24)   
#graficador(preciodx1,qdx1,preciodx2,qdx2,precioox1,qox1,precioox2,qox2)
    