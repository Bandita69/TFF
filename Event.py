from _datetime import datetime


preparation_time = 30
donation_time = 30

class EventData(object):

    # @Nori
    # Definition explanation comes here...
    @staticmethod
    def get_event_date():
        return True

    # @Nori
    # Definition explanation comes here...
    @staticmethod
    def get_donation_start():
        return True

    # @Bandi
    # Definition explanation comes here... A donation event vége. HH:MM formátmban, pl 12:10
    # NAGYOBBNAK KELL LENNIE MINT A don_start! (Work in progress)
    @staticmethod
    def get_donation_end():
        global don_end
        isvaild = False
        while not isvaild:
            data = input("Enter your End of donation (HH:MM):")
            try:
                don_end = datetime.strptime(data, "%H:%M") # Csak akkor engedi tovább az adatot ha ilyen formátumba van
                isvaild = True
            except ValueError:
                print(data, "is not a valid time! HH:MM. ex: 13:10")
        return don_end
    # @Bandi
    # Definition explanation comes here... nem nulla az első szám, és 4 karakter valamint csak számok.

    @staticmethod
    def get_zip_code():
        isvaild = False
        while not isvaild:
            ZIP = input("Enter your ZIP CODE (XXXX):")

            try:
                if int(ZIP) and len(ZIP) == 4:

                    if ZIP[0] != "0":
                        isvaild = True
                    else:
                        print(ZIP, "is not vaild! 1. number must not be 0!")
                else:
                    print("ZIP must be 4 digits!")
            except ValueError:

                print("Only Numbers!")
        return ZIP


    # @Atilla
    # Asks for the donor's city.
    @staticmethod
    def get_city():
        cities = ["Miskolc", "Kazincbarcika", "Szerencs", "Sarospatak"]
        # Asks for the input here first.
        city = input("Please enter the donor's city: ")
        # Keeps asking for the city while it does not match one from the cities list.
        while city not in cities:
            city = input("Donor's are accepted only from the following cities:\
            Miskolc, Kazincbarcika, Szerencs and Sarospatak: ")
        # Returns with the city.
        return city

    # @Atilla
    # Asks for the donor's address.
    @staticmethod
    def get_address():
        # Asks for the input here first.
        street = input("Please enter the donor's address: ")
        # Keeps asking for the address while it does not less or equal than 25 characters.
        while len(street) <= 25:
            street = input("The address should be less than 25 characters!: ")
        # Returns with the address.
        return street

    # @Mate
    # Definition explanation comes here...
    @staticmethod
    def get_available_beds():
        return True

    # @Mate
    # Definition explanation comes here...
    @staticmethod
    def get_planned_donor_number():
        return True

    # @Adam
    # Definition explanation comes here...
    @staticmethod
    def success_rate():
        return True