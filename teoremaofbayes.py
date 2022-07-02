import requests as rq
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# REGEX 
# Programa que va a sacar la probabilidad de 
# {Entro} Probabilidad de que un usuario entre a nuestra pagina (1.0006%) == 0.010006
# {Vulnerabilidad} Probabilidad de que un usuario encuentre una vulnerabilidad del (78%) == 0.78
# probabilidad de que alguien haga fuzzing, comunmento el {12%} hace fuzzing
# cual seria la probabilidad de que un usuario encuentre una vulnerabilidad, dado que
#que ha entrado en nuestra pagina
# (V)*(White/V) = 
#
# p(hackersPerCountry / country) = p(cvss) x p(hackersPerCountry|cvss) 
#                                                     p(totalPersonsPerCountryOnInternet)

# tables of avg from country that use internet
# https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users 

# Calcules necessaries for the calule the percentage of people per country

usersInternet = 5000000000000 # 100% People on internet.
totalUsersInRussia = 124000000 # Total users on internet from Russia.

# 100% -------> usersInternet
#   X  <-------- totalUserInRusssia

## RUSSIA  

cvss = 0.12
hackersPerCountry = 0.78 
totalPersonsPerCountryOnInternet = totalUsersInRussia * 100 / usersInternet  #The people in internet on Russia expressed by probability

## /RUSSIA
print (f'El resultado de esta verga es {totalPersonsPerCountryOnInternet}')
