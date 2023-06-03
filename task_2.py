# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и,
# если нет, вывести их на экран в порядке возрастания.

try:
    user_num_1 = int(input("Enter first number: "))
    user_num_2 = int(input("Enter second number: "))
    if user_num_1 == user_num_2:
        print(f"{user_num_1} = {user_num_2}")
    elif user_num_1 > user_num_2:
        print(f"{user_num_2}, {user_num_1}")
    else:
        print(f"{user_num_1}, {user_num_2}")
except ValueError as error:
    print("Enter only integer numbers please!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception: {error}")

