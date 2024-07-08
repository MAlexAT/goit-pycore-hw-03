from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            # If the birthday has already occurred this year, consider next year's date
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference between the birthday and today
        days_until_birthday = (birthday_this_year - today).days

        # Check if the birthday falls within the next 7 days
        if 0 <= days_until_birthday <= 7:
            # Adjust for weekends (move to next Monday if birthday falls on a weekend)
            if birthday_this_year.weekday() >= 5:  # Saturday or Sunday
                days_until_birthday += (7 - birthday_this_year.weekday())

            congratulation_date = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "Vsyl Petrenko", "birthday": "1983.07.10"},
    {"name": "Natalya Pushkar", "birthday": "1992.07.13"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
