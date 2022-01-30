n_floors = 3

def tower_builder(n_floors):
    buff_list = ['*']
    i = 1
    s = 0
    while i < n_floors:
        buff_list.append(buff_list[i-1] + '**')
        i = i + 1
    for element in buff_list:
        while len(buff_list[s]) < len(buff_list[-1]):
            buff_list[s] = ' ' + buff_list[s] + ' '
        s = s + 1

    print(buff_list)
    return buff_list

tower_builder(n_floors)