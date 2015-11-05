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
    # Definition explanation comes here...
    @staticmethod
    def get_donation_end():
        return True

    # @Bandi
    # Definition explanation comes here... nem nulla az ellső szám, és 4 karakter

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
                        print(ZIP, "in not vaild! 1. number must not be 0!")
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