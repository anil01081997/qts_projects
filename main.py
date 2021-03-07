from assignments import assign1_input, assign2_input_2, assign2_input_1


def first_assignment():
    print("-" * 50 + " Assignment - 1 " + "-" * 50)
    from anil_py.py_main import even_odd
    even_odd(assign1_input)
    from sourav_py.py_main import firstAssignment
    firstAssignment(assign1_input)


def second_assignment():
    print("-" * 50 + " Assignment - 2 " + "-" * 50)
    from sourav_py.py_main import secondAssign
    secondAssign(assign2_input_1, assign2_input_2)


first_assignment()
second_assignment()
