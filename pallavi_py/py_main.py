from assignments import assign1_input
def func(list_data):
    even = [i for i in list_data if i % 2 == 0]
    odd = [i for i in list_data if i % 2 == 1]

    print("Even numbers are", even)
    print("Odd numbers are", odd)

def func2(list_2,num):
    count=0
    for i in list_2:
        if i == num:
            count= count + 1
    return count