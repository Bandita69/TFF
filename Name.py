def i_need_your_name():
    global Name  # A f�g�vnyen k�v�l is lehet haszn�lni ezt a v�ltoz�t
    isvalid = False
    while not isvalid:
        Name = input("Enter your full name: ")

        split_Name = Name.split(" ")  # sz�tszedi a bek�rt adatot n�v r�szekre

        try:
            if Name.replace(" ", "").isalpha() and len(split_Name) > 1:  # A n�v legal�bb 2 r�szb�l �ll �s csak bet�ket tartlmazhat
                isvalid = True

            else:  # Ha pl sz�mokat adott meg  akkor ezt ki �rja �s �jra lek�ri.
                print("Try Again, it is not a name. The name can contain only letters and space! ex.: Angela Smith")
        except:
            pass

    return Name
i_need_your_name()
print(Name)