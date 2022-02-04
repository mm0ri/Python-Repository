sentence = ''

def order(sentence):
    s_buff = sentence.split(' ')
    res_list = []
    for i in range(len(s_buff)):
        res_list.append(i)

    for element in s_buff:
        for elem in element:
            if elem.isdigit():
                word_pos = int(elem)
                word_pos = word_pos - 1
                res_list.pop(word_pos)
                res_list.insert(word_pos,element)

    if type(res_list[0]) == int:
        result = ''
        return result
    else:
        result = ' '.join(res_list)
        return result

order(sentence)