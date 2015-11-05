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
    # Definition explanation comes here...
    @staticmethod
    def get_city():
        return True

    # @Atilla
    # Definition explanation comes here...
    @staticmethod
    def get_address():
        return True

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