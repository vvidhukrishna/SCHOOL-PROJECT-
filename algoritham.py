import random as r


def values_and_target(Number_of_Boxes, Difficulty):
    # choosing random numbers in the different boxes
    Number = [r.choice(range(1, 10)) for _ in range(Number_of_Boxes)]

    # choosing random operations for the numbers
    Operations = [str(r.choice(['+', '-', '*'])) for _ in range(Number_of_Boxes)]

    # creating box values
    Box_values = [Operations[k] + ' ' + str(Number[k]) for k in range(Number_of_Boxes)]

    # creating target
    cal = r.sample(Box_values, Difficulty)
    target = 1
    for i in cal:
        target = str(eval(str(target) + i))

    return tuple([Box_values, target])  # returning the values as tuples
