n_floors = 3

def tower_builder(n_floors):
    res_list = ['*']
    i = 0
    while i < n_floors:
        res_list.append(res_list[i] + '**')
        i = i + 1
        

tower_builder(n_floors)