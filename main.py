'''
Program ma za zadanie przepytywać z podanej listy słów.
Tłumaczenie z Polskiego na Angielski
'''

import random
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 130)
engine.setProperty('age', 20)
import csv

with open('data.csv', 'r',encoding='utf-8') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)
    word_list = list_of_csv

while True:
    # Poniżej następuje losowanie słowa.
    draw_an_english_word = random.choice(word_list)
    # Poniżej wartość [0] oznacza ze ma być wybrane tylko
    # Polskie słowo znajdujące się po lewej stronie pliku csv
    question = draw_an_english_word[0]

    # Prosi o wykonanie polecenia.
    print("Przetłumacz:", question)
    engine.say("Przetłumacz")
    engine.say(question)
    engine.runAndWait()
    answer = input("Podaj odpowiedź: ")
    answer = answer.lower()

    # Sprawdza wynik z listy. Wartość [1] to angielskie tłumaczenie.
    result = draw_an_english_word[1]
    result = result.lower()

    # instrukcja sprawdzająca wynik. Mówi także po angielsku by ćwiczyć wymowę.
    if answer == result:
        print("Odpowiedziałeś", answer.capitalize())
        engine.say("Odpowiedziałeś")
        engine.say(answer)
        engine.runAndWait()
    else:
        print("Źle! Prawidłowa odpowiedź to:", result.capitalize())
        engine.say("Źle! Prawidłowa odpowiedź to")
        engine.say(result)
        engine.runAndWait()
