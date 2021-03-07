from assignments import assign1_input, assign2_input_2, assign2_input_1


def first_assignment():
    print("-" * 50 + " Assignment - 1 " + "-" * 50)
    from anil_py.py_main import even_odd
    even_odd(assign1_input)

    from pallavi_py.py_main import assign_1
    assign_1(assign1_input)


def second_assignment():
    print("-" * 50 + " Assignment - 2 " + "-" * 50)
    from pallavi_py.py_main import assign_2
    assign_2(assign2_input_1, assign2_input_2)


first_assignment()
second_assignment()
