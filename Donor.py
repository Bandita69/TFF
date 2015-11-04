#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Az első két sor: Ékezetes/magyar karakterek engedélyezése

from datetime import datetime
# Beimportálja a datetime-t

from sys import exit
# Be importálja a sys.exit parancsot.(Nem megfelelő adat esetén kilép)
enter = "Enter your"
# Egy rövidítés

Blood_types = ["a", "b", "ab", "0"] # Blood Types kisbetűvel egy listában


class DonorData(object):
    @staticmethod
    # Weight
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

    """
    i_need_your_kg(): # Fügvény meghívása
    print(Weight)
    # Teszt hogy az a változó amit bekért

    if int(Weight) <= 50:
        exit("Sorry, you are not fat enough!")

        # Amennyiben nem teljesül a követelmény, kilép a program.
    """


    #Blood type
    def i_need_your_blood_type():
        global Blood  # a fügvényen kívül is használható
        isvalid = False  # Egy változó a try/except -hez
        while not isvalid:
            Blood = input("%s bloodtype(A,B,AB or 0): " % enter)
            try:
                if str(Blood).lower() in Blood_types:  # Amit beírt, átkonvertálja kisbetűvé és benne van e a Blood_types-ban
                    isvalid = True
                else:
                    print("Your bloodtype should be A , B , AB or 0! Try again!")
            except: # Ötletem nincs minek kell ez ide, de enélkül nem fut :D
                pass
        return Blood  # Ha helyes térjen vissza az adattal

    # Expiration of ID
    def i_need_your_exp():
        global date_of_exp   # a fügvényen kívül is használható
        isvaild = False  # Egy változó a try/except -hez
        while not isvaild:
            data = input("Type your exp date: yyyy/mm/dd: ") # Helyes adat pl.: 1999/10/10
            try:
                date_of_exp = datetime.strptime(data, "%Y/%m/%d") # Csak akkor engedi tovább az adatot ha ilyen formátumba van
                isvaild = True
            except:
                print("Try again! (yyyy/mm/dd) : \n")
        return date_of_exp

    """
    i_need_your_exp()  # Fügvény meghívása
    exp = i_need_your_exp()  # Változó a fügvénynek

    if exp < datetime.now():  # Ha a jelenlegi idő( . now) előtti a bekért adat
        exit("LEJART")   # Ki írja hogy Lejárt és kilép
    """











