from assignments import assign1_input, assign2_input_1, assign2_input_2, assign3_input


def first_assignment():
    print("\n"+"-" * 50 + " Assignment - 1 " + "-" * 50)
    print("Inputs :- \n", assign1_input, "\n\n")
    # from anil_py.py_main import even_odd
    # even_odd(assign1_input)

    from pratiksha_py.py_main import assignment1
    assignment1(assign1_input)


def second_assignment():
    print("\n"+"-" * 50 + " Assignment - 2 " + "-" * 50)
    print("Inputs :- \n", assign2_input_1, "\n", assign2_input_2, "\n\n")

    from pratiksha_py.py_main import assignment2
    assignment2(assign2_input_1,assign2_input_2)


def third_assignment():
    print("\n"+"-" * 50 + " Assignment - 3 " + "-" * 50)
    print("Inputs :- \n", assign3_input, "\n\n")
    from pratiksha_py.py_main import assignment3
    assignment3(assign3_input)

first_assignment()
second_assignment()
third_assignment()
