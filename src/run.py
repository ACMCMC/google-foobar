import random
import time

import scrape
import Query

search_result = None

queries_list = [Query.StandardQuery(), Query.ErrorQuery()]

while not (search_result == True):
    query = random.choice(queries_list)
    query = query.text()
    print("Vamos a buscar: " + query)
    scrape.scrape(query)
    time.sleep(1)

print("ÉXITO. SE HA ENCONTRADO UNA CAJA DE GOOGLE FOOBAR.")