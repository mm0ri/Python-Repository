morse_code = "...---..."

def decodeMorse(morse_code):

    second_list = []

    MORSE_CODE = {  '-.-.--':'!', '...---...': 'SOS', '/': ' ', '..-.': 'F', '-..-': 'X',
                    '.--.': 'P', '-': 'T', '..---': '2','.-.-.-':'.',
                    '....-': '4', '-----': '0', '--...': '7',
                    '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                    '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                    '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                    '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                    '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                    '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}


    morse_code = morse_code.replace('   ', ' / ')
    morse_code = morse_code.split(' ')

    count = 0
    for element in morse_code:
        for element in morse_code:

            if element == '':
                morse_code.remove('')
            elif morse_code[0] == '/':
                morse_code.pop(0)

        res = morse_code[count].replace(morse_code[count], MORSE_CODE[morse_code[count]])
        second_list.append(res)
        count = count + 1

    morse_code = ''.join(second_list)
    return morse_code

print(decodeMorse(morse_code))