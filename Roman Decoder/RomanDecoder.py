n = 2
def solution(n):

    resList = []
    n = str(n)
    thousands = 0
    hundreds = 0
    decades = 0
    units = 0
    
    ROMAN_CODE = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    thousands = thousands + ( int(n) // 1000 )
    while thousands > 0:
        thousands = thousands - 1
        resList.append(ROMAN_CODE[1000])

    hundreds = hundreds + int(n[-3])
    while hundreds > 0:
        if hundreds >= 5:
            hundreds = hundreds - 5
            resList.append(ROMAN_CODE[500])
        else:
            hundreds = hundreds - 1
            resList.append(ROMAN_CODE[100])

    decades = decades + int(n[-2])
    while decades > 0:
        if decades >= 5:
            decades = decades - 5
            resList.append(ROMAN_CODE[50])
        else:
            decades = decades - 1
            resList.append(ROMAN_CODE[10])

    units = units + int(n[-1])
    while units > 0:
        if units >= 5:
            units = units - 5
            resList.append(ROMAN_CODE[5])
        else:
            units = units - 1
            resList.append(ROMAN_CODE[1])

    result = "".join(resList)
    print(result)
    return result

solution(n)