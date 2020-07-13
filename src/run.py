import random
import time
import progressbar

import scrape
import Query

search_result = None

queries_list = [Query.StandardQuery(), Query.ErrorQuery()]

while not (search_result == True):
    query = random.choice(queries_list)
    query = query.text()
    print("Vamos a buscar: " + query)
    scrape.scrape(query)
    seconds_wait = random.randint(5,15)
    print("Waiting for", seconds_wait, "seconds")
    with progressbar.ProgressBar(max_value=seconds_wait) as bar:
        for x in range(seconds_wait):
            bar.update(x)
            time.sleep(1)

print("SUCCESS. A GOOGLE FOOBAR BOX HAS BEEN FOUND.")