#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Az első két sor: Ékezetes/magyar karakterek engedélyezése

import random
# Random beimpotálása
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

    @staticmethod
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

    @staticmethod
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
    # + Generate random number: Hemogblobin level between 80-200 , that must be higher than 110

    @staticmethod
    def hemo_level():
        global level # Fügvényen kívül is lehet használni
        level = (random.randrange(80,200))  # 80 és 200 között generáljon egy számot
        if level > 110:
            return level  # ha nagyobb mint 110 térjen vissza vele
        else:
            exit("Your Hemogblobin level is not high enough")  # ha kisebb mint 110 lépjen ki
    """
    hemo_level() # Fügvény meghívása
    """

    @staticmethod
    # Email address
    def get_email_address():        # The function asks for a valid email address
        global email_address
        isvalid = False

        while not isvalid:
            email_address = input("%s email address: " % enter)
            try:
                email_address_string = email_address.replace(" ", "")
                contains_at_sign = "@" in email_address_string and email_address_string.index("@") > 0
                ending_is_valid = email_address_string.endswith(".hu") or email_address_string.endswith(".com")

                isvalid = contains_at_sign and ending_is_valid

                if not isvalid:     # If any of the above conditions is False, it raises a ValueError
                    raise ValueError

            except ValueError:
                print("The given '%s' email address is not in a valid format. Try again! \n" % email_address)
        return email_address

    @staticmethod
    # Mobile number
    def get_mobile_number():        # The function asks for a valid mobile number
        global mobile_number
        isvalid = False

        while not isvalid:
            mobile_number = input("%s mobile number: " % enter)
            try:
                mobile_number_string = mobile_number.replace(" ", "")
                startswith_36_or_06 = mobile_number_string.startswith("+36") or mobile_number_string.startswith("06")
                contains_20_30_70 = "20" in mobile_number_string or "30" in mobile_number_string\
                                    or "70" in mobile_number_string
                valid_length = len(mobile_number_string) == 11

                isvalid = startswith_36_or_06 and contains_20_30_70 and valid_length

                if not isvalid:         # If any of the above conditions is False it raises a ValueError
                    raise ValueError

            except ValueError:
                print("The given '%s' mobile number is not in a valid format!" % mobile_number)

        return mobile_number

    @staticmethod
    def i_need_your_name():
        global name     # A fügévnyen kívül is lehet használni ezt a változót
        isvalid = False
        while not isvalid:
            name = input("Enter your full name: ")

            split_name = name.split(" ")        # Szétszedi a bekért adatot név részekre

            try:
                isvalid = name.replace(" ", "").isalpha()\
                          and len(split_name) > 1       # A név legalább 2 részből áll és csak betűket tartlmazhat

                if not isvalid:
                    raise ValueError

            except ValueError:      # Ha pl számokat adott meg  akkor ezt ki írja és újra lekéri.
                print("Try Again, it is not a name. The name can contain only letters and space! ex.: Angela Smith")

        return name

    @staticmethod
    def get_gender():
        global gender
        entered_data_is_valid = False
        available_genders = ["f", "m"]
        while not entered_data_is_valid:
            gender = input("Enter your sex: (F for Female/M for Male)")
            if gender.lower() in available_genders:
                entered_data_is_valid = True
            else:
                print("Try Again!")

        return gender.lower()








