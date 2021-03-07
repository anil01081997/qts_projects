def assign_1(list_data):
    print("Assignment 1 Solution by Pallavi " + "-" * 50)
    even = [i for i in list_data if i % 2 == 0]
    odd = [i for i in list_data if i % 2 == 1]

    print("Even numbers are", even)
    print("Odd numbers are", odd)


def assign_2(list_2, num):
    print("Assignment 2 Solution by Pallavi " + "-" * 50)
    count = 0
    for i in list_2:
        if i == num:
            count = count + 1
    print(count)
