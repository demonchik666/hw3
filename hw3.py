from datetime import datetime as dt
import re
import random

#Task 1
def get_days_from_today(date: str):
    today = dt.today()
    #transform the given string to datetime object
    try:
        date_datetime_object = dt.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return None
    #find the difference between the two dates
    delta = today - date_datetime_object
    return delta.days

# date = input("Enter a date in YYYY-MM-DD format: ")
# days = get_days_from_today(date)
# if days is not None:
#     print(f"Days from today to {date}: {days} days")

#Task 2
def get_numbers_ticket(min, max, quantity):
    #check the requirements
    if min < 1 or max > 1000 or quantity > (max - min) or min >= max:
        print("Invalid input. Please ensure 1 <= min < max <= 1000 and min <= quantity <= max.")
        return []
    #create a list of numbers from min to max
    numbers = []
    for i in range(min, max + 1):
        numbers.append(i)
    #tale random numbers from the list and sort them
    numbers = random.sample(numbers, quantity)
    numbers.sort()
    return numbers

# lottery_numbers = get_numbers_ticket(1, 1000, 15)
# print("Your lottery tickets:", lottery_numbers)

#Task 3
def normalize_phone(phone_number):
    # Remove everything except digits
    phone_number = re.sub(r"\D", "", phone_number)
    # check if phone number starts with 0. If it is a case, replace it with 380
    if phone_number.startswith("0"):
        phone_number = "380" + phone_number[1:]
    # check if phone number starts with 380. If it is still not a case, add 380 to the beginning
    if not phone_number.startswith("380"):
        phone_number = "380" + phone_number
    # add plus
    phone_number = "+" + phone_number
    return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+ 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Normalized phone numbers:", sanitized_numbers)




        
