import random
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0")
engine.setProperty("rate", 130)
engine.setProperty('age', 20)
word_list = [
    ('obywatelstwo', 'citizenship'),
    ('data urodzenia', 'date of birth'),
    ('wykształcenie', 'educational background'),
    ('kobieta, płeć żeńska', 'female'),
    ('imię i nazwisko', 'full name'),
    ('nazwisko panieńskie', 'maiden name'),
    ('stan cywilny', 'marital status'),
    ('narodowość', 'nationality'),
    ('w separacji', 'separated'),
    ('kawaler', 'single'),
    ('atrakcyjny,ładny', 'attractive'),
    ('przeciętny', 'average'),
    ('piękny', 'beautiful'),
    ('elegancki', 'elegant'),
    ('niechlujny', 'scruffy'),
    ('starszy w formie grzecznościowej', 'elderly'),
    ('młody', 'young'),



]
# warunek pętli
i = 0
while i < 1:
    losuj_pare_slow = random.choice(word_list)
    # tu jest losowany klucz.Wartosc okreslajaca pozycje w krotce.
    losuj_pare_kluczy = random.randint(0, 0)
    #tu jest wypisane question o przetlumaczenie slowa
    question = losuj_pare_slow[losuj_pare_kluczy]
    print("Przetłumacz", question)
    engine.say("Przetłumacz")
    engine.say(question)
    engine.runAndWait()
    answer = input("Podaj odpowiedź: ")
    answer = answer.lower()
# instrukcja sprawdzajaca wynik

    # musi sprawdz. Jezeli 0 to dodac 1. Jezeli 1 to -1.po czym sprawdzic czy sa rowne.
    # funkcja sprawdzajaca i zmniejszajaca lub zwiekszajaca klucz
    if losuj_pare_kluczy == 0:
        sprawdzwynik = losuj_pare_kluczy + 1
    else:
        sprawdzwynik = losuj_pare_kluczy -1

    koncowy_wynik = losuj_pare_slow[sprawdzwynik]
    koncowy_wynik = koncowy_wynik.lower()

    #
    if answer == koncowy_wynik:
        print("Odpowiedziałeś", answer)
        engine.say("Odpowiedziałeś ")
        engine.say(answer)
        engine.runAndWait()

    else:
        print("Źle! Prawidłowa odpowiedź to", koncowy_wynik)
        engine.say("Źle! Prawidłowa odpowiedź to ")
        engine.say(koncowy_wynik)


