import random
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 140)
engine.setProperty('age', 20)

lista_slowek = [
    ('Gold','Warm'),
    ('Speak','Cold'),
    ('Widow','Wind'),
    ('Spider','Table'),
]
# tu nastepuje losowania slowa z listy
losuj_pare_slow = random.choice(lista_slowek)
# tu jest losowany klucz.Wartosc okreslajaca pozycje w krotce.
losuj_pare_kluczy = random.randint(0,1)
#

#tu jest wypisane pytanie o przetlumaczenie slowa
pytanie = losuj_pare_slow[losuj_pare_kluczy]
print(pytanie)
engine.say("Podaj odpowiedź")
engine.runAndWait()
#twoj_wybor = input("Podaj odpowiedz")
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Słucham...")
    audio = r.listen(source)
    twoj_wybor = r.recognize_google(audio,language="pl-PL")
print(twoj_wybor)
twoj_wybor = twoj_wybor.lower()
print(twoj_wybor)
#instrukcja sprawdzajaca wynik

# musi sprawdz. Jezeli 0 to dodac 1. Jezeli 1 to -1.po czym sprawdzic czy sa rowne.
# funkcja sprawdzajaca i zmniejszajaca lub zwiekszajaca klucz
if losuj_pare_kluczy == 0:
    sprawdzwynik = losuj_pare_kluczy + 1
else:
    sprawdzwynik = losuj_pare_kluczy -1

print("Odpowiedz to",losuj_pare_slow[sprawdzwynik])
koncowy_wynik = losuj_pare_slow[sprawdzwynik]
koncowy_wynik = koncowy_wynik.lower()

#
if twoj_wybor == koncowy_wynik:
    print("brawo")
else:
    print("slabo")
print(sprawdzwynik)