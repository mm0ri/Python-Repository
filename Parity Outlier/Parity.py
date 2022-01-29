integers = [2,4,6,8,10,3]

def find_outlier(integers):
    even_buff = []
    odd_buff = []
    for element in integers:
        if (element % 2) == 0:
            even_buff.append(element)
        else:
            odd_buff.append(element)

    if len(even_buff) == 1:
        print(even_buff[0])
        return even_buff[0]
    else:
        print(odd_buff[0])
        return odd_buff[0]

find_outlier(integers)
