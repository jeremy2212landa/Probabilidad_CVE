#import requests as rq
import re
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


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


hackers_in_2016 = {
    'China':0.41,
    'United States':0.13,
    'Taiwan':0.044,
    'Russia':0.032,
    'Turkey':0.029,
    'South Korea':0.028,
    'India':0.024,
    'Brazil':0.023,
    'Germany':0.018,
    'Hong Kong':0.013
}

users_in_internet =  {
    'China':0.0142,
    'United States':0.0044,
    'Taiwan':0.0003,
    'Russia':0.0017,
    'Turkey':0.0010,
    'South Korea':0.0007,
    'India':0.0117,
    'Brazil':0.0023,
    'Germany':0.0011,
    'Hong Kong':0.0001
}



# tables of avg from country that use internet
# https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users 

# Calcules necessaries for the calule the percentage of people per country

usersInternet = 7100000000000 # 100% People on internet.
totalUsersInRussia = 124000000 # Total users on internet from Russia.

# 100% -------> usersInternet
#   X  <-------- totalUserInRusssia

## RUSSIA  

cvss = 0.12
hackersPerCountry = 0.78 
totalPersonsPerCountryOnInternet = totalUsersInRussia * 100 / usersInternet  #The people in internet on Russia expressed by probability

# p(hackersPerCountry / country) = p(cvss) x p(hackersPerCountry|cvss) 
#                                                     p(totalPersonsPerCountryOnInternet)

p = (cvss * hackers_in_2016['Russia']) / users_in_internet['Russia']

print (f'tu sistema es probable que sea hackeado por un hacker ruso un {p}')

## /RUSSIA
#print (f'El resultado de esta verga es {totalPersonsPerCountryOnInternet}')
