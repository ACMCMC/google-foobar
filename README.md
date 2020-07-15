# google-foobar
## [EN]
## Python 3 program to automatically perform google searches related to programming questions in order to get the Google Foobar challenge.

This program creates random questions based on a set of question makers:
- A question maker that searches Stack Overflow to randomly choose previously asked questions.
- A question maker that uses a set of pre-defined words to form questions of the form:
    ```how to + (verb) + (concept) + in + (programming language)```
    For example: "how to declare variables in Java".
- A question maker that creates questions of the form:
    ```(random number) + error in + (programming language)```

Using Selenium, the program searches those questions in Google Chrome or the user browser so that, eventually, the Google Foobar challenge may show up. At that point, the program stops and the user can take the challenge.

In order not to be detected as a bot, the program actually acceses one random result of the Google search and waits a random time between 5 and 15 seconds for each question asked. The best way to use the program is to just let it work overnight.

----

## [ES]
## Programa de Python 3 para realizar búsquedas automatizadas relacionadas con conceptos de programación para llegar challenge de Google Foobar.

----

Dependencies *(Dependencias)*:
- Selenium
- Progressbar2
- requests
- BeautifulSoup4
