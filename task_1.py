# 1. Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.

try:
    user_day = int(input("Enter a number from 1 to 7: "))
    if user_day == 1:
        print(f"{user_day}st day of the week is Monday")
    elif user_day == 2:
        print(f"{user_day}nd day of the week is Tuesday")
    elif user_day == 3:
        print(f"{user_day}rd day of the week is Wednesday")
    elif user_day == 4:
        print(f"{user_day}th day of the week is Thursday ")
    elif user_day == 5:
        print(f"{user_day}th day of the week is Friday")
    elif user_day == 6:
        print(f"{user_day}th day of the week is Saturday")
    elif user_day == 7:
        print(f"{user_day}th day of the week is Sunday")
    else:
        raise Exception("Please enter number from 1 to 7")
except ValueError as error:
    print("Please, enter only int numbers")
except Exception as error:
    print("Please, enter int from 1 to 7")
