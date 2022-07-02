import requests as rq
import re
#import pandas as pd
#import numpy as np
#import matplotly as plt


# REGEX 
# Programa que va a sacar la probabilidad de 
# {Entro} Probabilidad de que un usuario entre a nuestra pagina (1.0006%) == 0.010006
# {Vulnerabilidad} Probabilidad de que un usuario encuentre una vulnerabilidad del (78%) == 0.78
# probabilidad de que alguien haga fuzzing, comunmento el {12%} hace fuzzing
# cual seria la probabilidad de que un usuario encuentre una vulnerabilidad, dado que


vuln = 0.78 #probabilidad
fuzz = 0.12 #fuzz
entro = 0.010006 #entro





resultado = (vuln * (entro/vuln))/entro

print (f'El resultado de esta verga es {resultado}')
#que ha entrado en nuestra pagina
# (V)*(White/V) = 
# white ()
# p( vulnerabilidad | Entro ) = p(v) . p(e|v) 
#                                   p(e)
# 