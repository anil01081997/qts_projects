def even_odd(test_list):
    print("Solution By Master-----------")
    print("Even numbers in the list are " + ", ".join(str(data) for data in test_list if data % 2 == 0))
    print("Odd numbers in the list are " + ", ".join(str(data) for data in test_list if data % 2 == 1))
