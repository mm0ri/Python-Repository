s = 'abcdef'
res_list = []

def solution(s):
    i = 0
    first_pos = 0 
    res_len = len(s)

    while i < res_len:
        if (len(s) % 2) == 0:
            second_pos = first_pos + 2
            s_buff = s[first_pos:second_pos]
            res_list.append(s_buff)

            first_pos = first_pos + 2
            second_pos = second_pos + 2
            i = i + 2
            print(res_list)
        else:
            None
solution(s)