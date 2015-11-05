def get_date(name_of_date: str):
	date_string = ""
	while not date_string:
	date_string = get_string_from_console
	if not date_string_is_valid(date_string):
		print("Correct form: YYYY.MM.DD")
		date string = ""

	return parse_date_string(date_string)

