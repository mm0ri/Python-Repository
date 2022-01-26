string_ = 'This website is for losers LOL!'

def disemvowel(string_):
    vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    buff_list = []
    for element in string_:
        if element in vowel_list:
            continue
        else:
            buff_list.append(element)
    
    string_ =''.join(buff_list)
    return string_

disemvowel(string_)