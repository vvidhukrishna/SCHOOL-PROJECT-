import random as r


def values_and_target(Number_of_Boxes, Difficulty):
    # choosing random numbers in the different boxes
    Number = [r.choice(range(-10, 10)) for _ in range(Number_of_Boxes)]

    # choosing random operations for the numbers
    Operations = [str(r.choice(['+', '-', '*'])) for _ in range(Number_of_Boxes)]

    # creating box values
    Box_values = [Operations[k] + ' ' + str(Number[k]) for k in range(Number_of_Boxes)]

    # replacing double negative numbers with positive numbers, e.g: - -1 => +1
    for i, j in enumerate(Box_values):
        if '- -' in j:
            new_num = '+ ' + j[-1]
            Box_values.pop(i)
            Box_values.insert(i, new_num)

        if '+ -' in j:
            new_num = '- ' + j[-1]
            Box_values.pop(i)
            Box_values.insert(i, new_num)

    # creating target
    cal = r.sample(Box_values, Difficulty)
    target = 1
    for i in cal:
        target = str(eval(str(target) + i))

    return tuple([Box_values, target])  # returning the values as tuples
