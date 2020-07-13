FILE_TERMS = "raw_terms.json"

import json
import random

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
