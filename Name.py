def i_need_your_name():
    global Name  # A fügévnyen kívül is lehet használni ezt a változót
    isvalid = False
    while not isvalid:
        Name = input("Enter your full name: ")

        split_Name = Name.split(" ")  # szétszedi a bekért adatot név részekre

        try:
            if Name.replace(" ", "").isalpha() and len(split_Name) > 1:  # A név legalább 2 részbõl áll és csak betûket tartlmazhat
                isvalid = True

            else:  # Ha pl számokat adott meg  akkor ezt ki írja és újra lekéri.
                print("Try Again, it is not a name. The name can contain only letters and space! ex.: Angela Smith")
        except:
            pass

    return Name
i_need_your_name()
print(Name)