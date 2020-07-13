FILE_TERMS = "raw_terms.json"

import json
import random

import requests #Esto lo usamos para el StackOverflowQuery
from bs4 import BeautifulSoup

class Query:
    def text(self):
        return "Test text"
    pass

class SelfFormedQuery(Query):
    def extractJSON(self):
        with open(FILE_TERMS, "r") as file:
            data = json.load(file)
        return data["list"] #the first index of the JSON file is a list of all lists of words, so we take that
    pass

class StackOverflowQuery(Query):
    SEARCH_URL = "https://stackoverflow.com/questions?tab=newest&page="
    def text(self):
        results_page = requests.get(self.SEARCH_URL+str(random.randint(1,1000))) #We load a random page of Stack Overflow questions (from 1 to 1000)

        if results_page.status_code != 200:
            print("Something went wrong. Got HTTP status code", results_page.status_code) #In case we don't get an HTTP 200

        parser = BeautifulSoup(results_page.text, 'html.parser') #We create our parser object

        return random.choice(parser.find(id="questions").find_all("a", class_="question-hyperlink")).contents[0] #The result of this function is a string which is one of the questions (randomly chosen) of a Stack Overflow questions page
    pass

class ErrorQuery(SelfFormedQuery):
    def text(self):
        error_code = random.randint(0x0,0xffffffff)
        data = self.extractJSON()
        language = random.choice(list(filter(lambda x: x["type"] == "language_names", data))[0]["word_list"])
        return(" ".join([language, "error", hex(error_code)]))

class StandardQuery(SelfFormedQuery):
    def text(self):
        data = self.extractJSON()
        verb = random.choice(list(filter(lambda x: x["type"] == "verbs", data))[0]["word_list"])
        language = random.choice(list(filter(lambda x: x["type"] == "language_names", data))[0]["word_list"])
        concept = random.choice(list(filter(lambda x: x["type"] == "concepts", data))[0]["word_list"])
        return(" ".join(["how to", verb, concept, "in", language]))

    pass
