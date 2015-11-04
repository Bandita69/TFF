def get_string_from_console(name_of_data: str, form_instruction=""):

    data_string = ""
    while not data_string:
        data_string = input("{0} {1}{2}:".format(ENTER_DATA_TEXT, name_of_data, form_instruction))
        if not data_string:
            print("This can't be empty!")

    return data_string

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