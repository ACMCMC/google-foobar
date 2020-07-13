import requests
from bs4 import BeautifulSoup

SEARCH_URL = "https://www.google.com/search?q=" #this is the base URL, to which we have to join the search query

def scrape(search_query): #search_query is a string of words we want to use to search for (related to programming questions), separated by spaces

    #load the search URL
    results_page = requests.get(SEARCH_URL+search_query.replace(" ","+"))
    print("Getting:", SEARCH_URL+search_query.replace(" ","+"))

    #we return TRUE if we found the result we wanted (the Google Foobar box)

    #by default, our search has not been successful
    return False