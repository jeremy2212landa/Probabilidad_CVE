import numpy as np
import matplotlib.pyplot as plt
import tkinter

def probability(hackers_in_2016, cvss, usersInternet):
    
    valuesHackers = []
    valuesCountries = []
    others = 0
    
    for index in hackers_in_2016:
        p = round((cvss * hackers_in_2016[index]) / usersInternet, 4)
        
        valuesHackers.append(p)
        valuesCountries.append(index)
        others = others + p
    
    valuesHackers.append(others)
    valuesCountries.append('Others')
      
    return valuesHackers, valuesCountries

# Creating autocpt arguments
def percentage(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n".format(pct, absolute)

def acumValues(pieValues, labels, cvss):
    # Creating explode data
    explode = (0.1, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.2, 0.3, 0.05)
    # Colors
    colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige", "pink")
    
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize =(10, 6))
    # Dibujar puntos
    ax.set_title("""Propability top 10 that a hacker from 
    these countries hacked you, with a CVSS of: """ + str(cvss), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue', 'verticalalignment': 'baseline',})
    # Set the values of the grafic
#    ax.pie(pieValues)
    ax.pie(pieValues,
        autopct = lambda pct: percentage(pct, pieValues),
        explode = explode,
        labels = labels,
        shadow = True,
        colors = colors,
        startangle = 90,
        wedgeprops = wp,)
    # Put the legends location, position and labels
    ax.legend(loc = 'best', bbox_to_anchor=(-0.7, -0.5, 0.5, 1), labels = labels, title ="Countries")
    
    # Guardar el gráfico en formato png
    #input = input('Ingrese la ruta de guardado') f'{input}/
    plt.savefig('diagrama-hackers.png')
    # Mostrar el gráfico
    plt.show()
    
"""  
## Make the pie/grafic
dobleArray = probability()

print(dobleArray[0])
print(dobleArray[1])

acumValues(dobleArray[0], dobleArray[1]) """


def kinter(hackers_in_2016, usersInternet):
    root = tkinter.Tk()

    root.geometry('400x400')
    texto = tkinter.Label(root, text = 'CVSS')
    input = tkinter.Entry(root)

    def obtenerCVSS():
        cvss = float(input.get())
        dobleArray = probability(hackers_in_2016, cvss, usersInternet)
        acumValues(dobleArray[0], dobleArray[1], cvss)

    btn = tkinter.Button(root, text = 'Enter', command = lambda: obtenerCVSS())

    texto.pack()
    input.pack()
    btn.pack()




    #Run the loop
    root.mainloop()