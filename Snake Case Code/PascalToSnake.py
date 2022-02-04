import re

string = 1

def to_underscore(string):
    if type(string) != str:
        string = str(string)
        
    rex = re.sub(r'([A-Z])', r' \1', string).split()
    if type(rex[0]) == int:
        res = str(rex)
        print(type(res))
    else:
        res = '_'.join(rex).lower()
        print(type(res),res)
        return res

to_underscore(string)