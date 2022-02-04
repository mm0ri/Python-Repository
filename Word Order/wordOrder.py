sentence = 'is2 Thi1s T4est 3a'

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


order(sentence)