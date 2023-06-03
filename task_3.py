# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат.

try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    user_choice = int(input("Enter 1 for +,\n 2 for -\n 3 for *\n 4 for /: "))
    if user_choice == 1:
        result = num_1 + num_2
        print(f"result: {result}")
    elif user_choice == 2:
        result = num_1 - num_2
        print(f"result: {result}")
    elif user_choice == 3:
        result = num_1 * num_2
        print(f"result: {result}")
    elif user_choice == 4:
        result = num_1 / num_2
        print(f"result: {result}")
    else:
        raise Exception("Please, enter number from 1 to 4")
except ZeroDivisionError as error:
    print("division on 0")
except ValueError as error:
    print("Please, input int")
except Exception as error:
    print(f"Error: {error}")
