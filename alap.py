#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Az első két sor: Ékezetes/magyar karakterek engedélyezése

from sys import exit
# Be importálja a sys.exit parancsot.(Nem megfelelő adat esetén kilép)
enter = "Enter your"
# Egy rövidítés


def i_need_your_kg():
    global Weight  # a fügvényen kívül is használható
    isvalid = False  # Egy változó a try/except -hez
    while not isvalid:  # Amíg nem igaz
        Weight = input("%s weight(ex.: 69): " % enter)
        try:  # Hogy a bekért adat egész szám
            int(Weight)
            isvalid = True
        except ValueError:  # Próbálja újra
            print("Nice, but", Weight, "is not a egész number. Try again! \n")
    return Weight  # Ha helyes térjen vissza az adattal



i_need_your_kg()

# Fügvény meghívása

print(Weight)
# Teszt hogy az a változó amit bekért

if int(Weight) <= 50:
    exit("Sorry, you are not fat enough!")

    # Amennyiben nem teljesül a követelmény, kilép a program.


