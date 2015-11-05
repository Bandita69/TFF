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
    # Definition explanation comes here...
    @staticmethod
    def get_zip_code():
        return True

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