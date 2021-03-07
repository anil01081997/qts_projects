def firstAssignment(assign1_input):
    print('solution by sourav' + "-" * 50)
    even_str = "Even numbers are:"
    odd_str = "Odd numbers are:"
    even_list = []
    odd_list = []
    for num in assign1_input:
        if num % 2 == 0:
            even_list.append(str(num))
        else:
            odd_list.append(str(num))
    print(even_str)
    print(odd_str)


def secondAssign(assign2_input_1, x):
    print('2nd solution by sourav' + "-" * 50)
    count = 0

    for lest in assign2_input_1:
        if (lest == x):
            count = count + 1
    print("the number of occurrences of x is:-", count)
