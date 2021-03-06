from selenium import webdriver

SEARCH_URL = "https://www.google.com/search?q=" #this is the base URL, to which we have to join the search query

#TODO: Implement the web scraper with Selenium instead of requests+bautifulsoup, because even though they do get the webpage, we need the user to be logged in his Google account for him to be able to access the Google Foobar challenge again. Selenium uses the standard OS browser, so it's better that way.

def scrape(search_query): #search_query is a string of words we want to use to search for (related to programming questions), separated by spaces

    #load the search URL
    driver = webdriver.Chrome("./chromedriver")
    driver.get(SEARCH_URL+search_query.replace(" ","+"))

    print(driver.title)

    #we return TRUE if we found the result we wanted (the Google Foobar box)

    #by default, our search has not been successful
    return False