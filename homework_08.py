from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now()  # Bieżąca data
    current_week_start = today - timedelta(
        days=today.weekday()
    )  # Start tygodnia (poniedziałek)
    next_week_start = current_week_start + timedelta(
        days=7
    )  # Początek kolejnego tygodnia

    birthday_users = []  # Uzytkownicy mający urodziny w tym tygodniu

    for user in users:  # Sprawdzenie kto ma urodziny w tym tygodniu
        user_birthday = user["birthday"].replace(
            year=today.year
        )  # Ustawienie bieżącego roku dla daty urodzin
        if current_week_start <= user_birthday < next_week_start:
            birthday_users.append(user)

    # Grupowanie użytkowników według dnia tygodnia
    grouped_birthdays = {}
    for user in birthday_users:
        birthday_day = user["birthday"].strftime("%A")
        if birthday_day in grouped_birthdays:
            grouped_birthdays[birthday_day].append(user["name"])
        else:
            grouped_birthdays[birthday_day] = [user["name"]]

    # Wyświetlanie użytkowników obchodzących urodziny według dnia tygodnia
    for day, names in grouped_birthdays.items():
        print(f"{day}: {', '.join(names)}")


# Przykładowa lista użytkowników
users = [
    {"name": "Bill", "birthday": datetime(2024, 1, 15)},
    {"name": "Joe", "birthday": datetime(2024, 1, 20)},
    {"name": "Kate", "birthday": datetime(2024, 1, 25)},
    {"name": "Tom", "birthday": datetime(2024, 1, 27)},
    {"name": "Frank", "birthday": datetime(2024, 1, 27)},
    {"name": "Liss", "birthday": datetime(2024, 1, 30)},
    {"name": "Mike", "birthday": datetime(2024, 2, 3)},
    {"name": "Jon", "birthday": datetime(2024, 3, 5)},
]

get_birthdays_per_week(users)
