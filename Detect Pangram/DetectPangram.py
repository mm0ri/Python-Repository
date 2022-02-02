s = 'Aacdefghijklmnopqrstuvwxyz'

def is_pangram(s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    for char in alph:
        if char not in s.lower():
            print("False")
            return False
        else:
            print("True")
            return True

is_pangram(s)