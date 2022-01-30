n_floors = 3

def tower_builder(n_floors):
    res_list = ['*']
    i = 1
    while i < n_floors:
        res_list.append(res_list[i-1] + '**')
        i = i + 1
    print(res_list)

tower_builder(n_floors)