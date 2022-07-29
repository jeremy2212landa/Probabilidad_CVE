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
    
    valuesHackers.append(usersInternet - others)
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
          "grey", "indigo", "beige", "pink", "blue", "yellow", "turquoise", "chocolate")
    
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize =(15, 10))
    # Dibujar puntos
    ax.set_title("""Propability top 10 that a hacker from 
    these countries hacked you, with a CVSS of: """ + str(cvss), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue', 'verticalalignment': 'baseline',})
    # Set the values of the grafic
#    ax.pie(pieValues)
    ax.pie(pieValues,
        autopct = lambda pct: percentage(pct, pieValues),
        explode = explode,
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

def probabilityCvss(comunCvss, hacker, hackersIntheWorld):
    valuesHackers = []
    valuesCvss = []
    others = 0
    
    for index in comunCvss:
        p = round((hacker * comunCvss[index]) / hackersIntheWorld, 4)
        
        valuesHackers.append(p)
        valuesCvss.append(index)
        others = others + p
        
    print(hackersIntheWorld - others)   
    #others = 1.00 - others
    valuesHackers.append(hackersIntheWorld - others)
    valuesCvss.append('No')
    
    return valuesHackers, valuesCvss
    
def acumValues2(plotValues, labels, country='China'):
    # Creating explode data
    explode = (0.1, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3, 0.2, 0.3, 0.05)
    # Colors
    colors = ( "orange", "cyan", "brown",
          "grey", "indigo", "beige", "pink", "blue", "yellow", "turquoise", "chocolate")
    
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize =(15, 10))
    # Dibujar puntos
    ax.set_title(f"""Propability that one person from {country} hacked you
                 take it on acount the propability of earn a error CVSS""", loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue', 'verticalalignment': 'baseline',})
    # Set the values of the grafic
#    ax.pie(pieValues)
    ax.pie(plotValues,
        autopct = lambda pct: percentage(pct, plotValues),
        explode = explode,
        colors = colors,
        startangle = 90,
        wedgeprops = wp,)
    
    # Put the legends location, position and labels
    ax.legend(loc = 'best', bbox_to_anchor=(-0.7, -0.5, 0.5, 1), labels = labels, title ="CVSS")
    
    # Guardar el gráfico en formato png
    #input = input('Ingrese la ruta de guardado') f'{input}/
    plt.savefig('diagrama-cvss.png')
    # Mostrar el gráfico
    plt.show()

def kinter(hackers_in_2016, usersInternet, comunCvss):
    root = tkinter.Tk()

    root.geometry('600x600')
    texto2 = tkinter.Label(root, text = 'Teorema of Bayes In Hacking')
    texto = tkinter.Label(root, text = 'CVSS')
    input = tkinter.Entry(root)

    def obtenerCVSS():
        cvss = float(input.get())
        dobleArray = probability(hackers_in_2016, cvss, usersInternet)
        acumValues(dobleArray[0], dobleArray[1], cvss)

    def obtenerhacker():
        hacker = float(input.get())
        dobleArray = probabilityCvss(comunCvss, hacker, usersInternet)
        acumValues2(dobleArray[0], dobleArray[1])

    btn = tkinter.Button(root, text = 'Probability per cvss', command = lambda: obtenerCVSS())
    btn2 = tkinter.Button(root, text = 'Probability per country', command = lambda: obtenerhacker())
    texto2.pack()
    texto.pack()
    input.pack()
    btn.pack()
    btn2.pack()




    #Run the loop
    root.mainloop()