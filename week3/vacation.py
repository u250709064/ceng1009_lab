start_day = int(input("enter the day:"))
vacation_length = int(input("enter the length of vacation:"))
total = start_day + vacation_length
end_day= total%7
print(f"your vacation ends on the day{end_day}")