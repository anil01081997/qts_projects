def assignment1(n):
    even_str="Even numbers are: "
    odd_str="Odd numbers are: "
    even_list=list()
    odd_list=list()
    for i in n:
        if i%2==0:
            even_list.append(str(i))
        else:
            odd_list.append(str(i))
    print(even_str + (' , ').join(even_list))
    print(odd_str + (' , ').join(odd_list))

def assignment2(list,n):
    print("slolution of assignment 2 by Pratiksha"+"-"*50)
    count=0
    for i in list:
        if i==n:
            count=count+1
        print(count)
