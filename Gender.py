def get_gender():
    entered_data_is_valid = False
    gender = ""
    available_genders = ["f", "m"]
    while not entered_data_is_valid:
        gender = get_string_from_console("gender", " (F/M)")
        if gender.lower() in available_genders:
            entered_data_is_valid = True

    return gender.lower()
