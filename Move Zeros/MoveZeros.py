array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

def move_zeros(array):
    for element in array:
        if element == 0:
            array.remove(element)
            array.append(element)

    print(array)
    return array

move_zeros(array)