s = 'Aacdefghijklmnopqrstuvwxyz'

def is_pangram(s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    for char in alph:
        print(char)
        if char not in s.lower():
            print("False")
            return False
    return True

is_pangram(s)