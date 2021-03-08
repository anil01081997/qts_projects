from assignments import assign1_input, assign2_input_1, assign2_input_2, assign3_input


def first_assignment():
    print("\n"+"-" * 50 + " Assignment - 1 " + "-" * 50)
    print("Inputs :- \n", assign1_input, "\n\n")
    from anil_py.py_main import even_odd
    even_odd(assign1_input)
    from sourav_py.py_main import firstAssignment
    firstAssignment(assign1_input)


def second_assignment():
    print("\n"+"-" * 50 + " Assignment - 2 " + "-" * 50)
    print("Inputs :- \n", assign2_input_1, "\n", assign2_input_2, "\n\n")
    from sourav_py.py_main import secondAssign
    secondAssign(assign2_input_1, assign2_input_2)


def third_assignment():
    print("\n"+"-" * 50 + " Assignment - 3 " + "-" * 50)
    print("Inputs :- \n", assign3_input, "\n\n")


first_assignment()
second_assignment()
third_assignment()
