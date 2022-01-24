string = "samurai"
ending = "ra"

def solution(string,ending):
    rlen = (len(string) - len(ending))
    res = string.find(ending,rlen)

    if res == -1:
        print("False")
        return False
    else:
        print("True")
        return True

solution(string,ending)