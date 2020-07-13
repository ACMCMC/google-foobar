import random
import time
import re

import Query

SEARCH_URL = "https://www.google.com/search?q=" #this is the base URL, to which we have to join the search query

def scrape(search_query): #search_query is a string of words we want to use to search for (related to programming questions), separated by spaces

    #load the search URL

    #we return TRUE if we found the result we wanted (the Google Foobar box)

    #by default, our search has not been successful
    return False

search_result = None

queries_list = [Query.StandardQuery(), Query.ErrorQuery()]

while not (search_result == True):
    query = random.choice(queries_list)
    query = query.text()
    print("Vamos a buscar: " + query)
    scrape(query)
    time.sleep(1)

print("ÉXITO. SE HA ENCONTRADO UNA CAJA DE GOOGLE FOOBAR.")