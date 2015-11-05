start_time = None
while start_time_string == "":
    start_time_string = input("Start time:")
    if is_time(start_time_string) and check_start_time(start_time_string):
        start_time = parse_date(start_time_string)
    else:
        print("Start time isnt correct.")
        start_time_string = ""
