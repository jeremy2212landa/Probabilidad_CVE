from functions import *

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

usersInternet = 1.00 # 100% People on internet.
hackersIntheWorld = 1.00 # 100% Hackers on the world

comunCvss = {
    'A01:2021':0.0381,
    'A02:2021':0.18,
    'C22:2021':0.4,
    'F02:2021':0.32,
    'U02:2021':0.29,
    'O02:2021':0.28,
    'E02:2021':0.24,
    'A52:2021':0.23,
    'A32:2021':0.18,
    'A12:2021':0.13
}

#hacker = 0.028

#example = probabilityCvss(comunCvss, hacker, hackersIntheWorld)

#acumValues2(example[0], example[1])

kinter(hackers_in_2016, usersInternet, comunCvss)

# This data, i think that isn't necessary 
# """
# users_in_internet =  {
#     'China':0.0142,
#     'United States':0.0044,
#     'Taiwan':0.0003,
#     'Russia':0.0017,
#     'Turkey':0.0010,
#     'South Korea':0.0007,
#     'India':0.0117,
#     'Brazil':0.0023,
#     'Germany':0.0011,
#     'Hong Kong':0.0001
# }
# """

# tables of avg from country that use internet
# https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users 

# Calcules necessaries for the calule the percentage of people per country

#tables of hackers come from country 
# https://www.cyberkite.com.au/post/hackers-top-10-countries-where-they-come-from-hacker-types


# 100% -------> usersInternet
#   X  <-------- totalUserInRusssia

## RUSSIA  
 #Dates that will be get by a file .cvs
#totalPersonsPerCountryOnInternet = totalUsersInRussia * 100 / usersInternet  
#The people in internet on Russia expressed by probability

# p(hackersPerCountry / country) = p(cvss) x p(hackersPerCountry|cvss) 
#                                  p(totalPersonsPerCountryOnInternet)


# #Example for the function probability(i, v, r)
# dobleArray = probability(hackers_in_2016, cvss, usersInternet)

# print(dobleArray)
# #print(dobleArray[0])
# #print(dobleArray[1])
# acumValues(dobleArray[0], dobleArray[1], cvss)





