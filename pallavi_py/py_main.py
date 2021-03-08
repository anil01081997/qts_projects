from assignments import assign1_input
def assignment_1(list_data):
    print("Solution of assignment 1 by pallavi"+"-"*50)
    even = [i for i in list_data if i % 2 == 0]
    odd = [i for i in list_data if i % 2 == 1]

    print("Even numbers are", even)
    print("Odd numbers are", odd)

def assignment_2(list_2,num):
    print("Solution of assignment 2 by pallavi"+"-"*50)
    count=0
    for i in list_2:
        if i == num:
            count= count + 1
    print(count)