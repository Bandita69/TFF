def name_is_valid(name_string: str):
    splitted_name = name_string.split(" ")
    return name_string.replace(" ", "").isalpha() and len(splitted_name) > 1


def get_name():
    entered_data_is_valid = False
    name_string = ""
    name_form_instruction = " (FirstName LastName)"

    while not entered_data_is_valid:
        name_string = get_string_from_console("name", name_form_instruction)
        if name_is_valid(name_string):
            entered_data_is_valid = True
        else:
            print("The name can contain only letters and space!".format(name_form_instruction))

    return name_string