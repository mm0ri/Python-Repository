s = 'abcdef'

def solution(s):
    i = 0
    first_pos = 0
    res_list = []
    res_len = len(s)

    if (len(s) % 2) != 0:
            s = s + '_'

    while i < res_len:
            second_pos = first_pos + 2
            s_buff = s[first_pos:second_pos]
            res_list.append(s_buff)

            first_pos = first_pos + 2
            second_pos = second_pos + 2
            i = i + 2

    return res_list

solution(s)