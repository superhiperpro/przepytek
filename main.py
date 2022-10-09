""" 
import csv

print("Witaj. Przepytam Cię ze słówek. Jeżeli chcesz zacząć wciśnij 1")
decyzja = input()
if decyzja == "1":
    print("start")
else: print("błąd. Dokonaj wyboru")

"""
import csv
import random
en_to_pl = {}
pl_to_en = {}
""""""

with open('data.txt', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # oryginalny słownik z danymi pl -> eng
  en_to_pl = {row[0]: row[1] for row in reader}
  # odwracamy słownik żeby móc tłumaczyć w drugą stronę (pl -> en)
  # to raczej będzie szybsze niż ponowne czytanie pliku
  pl_to_en = {value: key for key, value in en_to_pl.items()}

#test czy wyświetla
print("to tylko test",pl_to_en["zimno"])
#
def komputer_losuje():
    losowanie = pl_to_en
    wynik = (random.choice(losowanie))
    return wynik


wynik = komputer_losuje()
print(wynik)


print("Podaj odpowiedź po angielsku")
sprawdz = input()
if sprawdz in en_to_pl:
    print("dobrze")
else: print("zle")