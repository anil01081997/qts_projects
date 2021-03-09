from assignments import assign1_input

def assignment_1(list_data):
    print("Solution of assignment 1 by pallavi"+"-"*50)
    even_str = 'Even numbers are '
    odd_str = 'Odd numbers are '
    even=[]
    odd=[]
    for i in list_data:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    print(even_str + (',').join(even))
    print(odd_str + (',').join(odd))

def assignment_2(list_2,num):

    print("Solution of assignment 2 by pallavi"+"-"*50)
    count=0
    for i in list_2:
        if i == num:
            count = count + 1
    print(count)

def assignment_3(n):
    print("Solution of assignment 3 by pallavi"+"-"*50)
    for i in range(1,n+2):
        for j in range(i,n+1):
            print(i,end=' ')
        print()