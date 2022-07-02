import numpy as np
import matplotlib.pyplot as plt

def probability(hackers_in_2016, cvss, usersInternet):
    
    valuesHackers = []
    valuesCountries = []
    
    for index in hackers_in_2016:
        p = round((cvss * hackers_in_2016[index]) / usersInternet, 4)
        percentage = round(p * 100, 4)

        valuesHackers.append(percentage)
        valuesCountries.append(index)
        
       # print (f"""
            #Tu sistema es probable que sea hackeado por un hacker de {index} una probabilidad de {p},
            # expresada con un porcentaje de {percentage} %,
            #todo esto cuando el CVSS sea de: {cvss}
       # """)
      
    return valuesHackers, valuesCountries

def acumValues(pieValues, labels):
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    # Dibujar puntos
    ax.set_title('Hackers to the long of the time', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    
    ax.pie(pieValues)
    ax.legend(loc = 'best', bbox_to_anchor=(-0.45, -0.5, 0.5, 1), labels = labels)
    
    # Guardar el gráfico en formato png
    plt.savefig('diagrama-hackers.png')
    # Mostrar el gráfico
    plt.show()
    
"""  
## Make the pie/grafic
dobleArray = probability()

print(dobleArray[0])
print(dobleArray[1])

acumValues(dobleArray[0], dobleArray[1]) """