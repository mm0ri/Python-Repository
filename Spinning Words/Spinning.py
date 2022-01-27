sentence = 'Something in the water'

def spin_words(sentence):
    buff_list = sentence.split()
    sec_list = []
    for element in buff_list:
        if len(element) >= 5:
            sec_list.append(element[::-1])
        else:
            sec_list.append(element)

    res = ' '.join(sec_list)
    return res

spin_words(sentence)