HEX_CODE = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
r,g,b = 148, 0, 211

def rgb(r,g,b):
    rgb_list = [r,g,b]
    res_list = []

    for elem in rgb_list:
        buff_elem = str(elem / 16).split('.')
        buff_elem[1] = str(16 * float('0.' + buff_elem[1])).replace('.0', '')
        for elem in range(len(buff_elem)):
            res_list.append(buff_elem[elem].replace(buff_elem[elem], HEX_CODE[buff_elem[elem]]))
    return ''.join(res_list)

rgb(r,g,b)
