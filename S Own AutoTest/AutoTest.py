import subprocess as sb

# Функция запуска дополнительного процесса

def main_proc():

    test_list = [10, 'a', 72] # Тестовые значения, может быть сколько угодно.
    buff_list = []
    res_list = []
    re_list = []

    for elem in test_list:
            elem = str(elem)
            if elem.isdigit():
                buff_list.append(sb.check_output(['python3', 'MainProg.py', elem]))

    # Цикл отделения лишних данных от числовых данных

    for elem in buff_list:
        buff = str(elem)
        num = ''
        for char in buff:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    res_list.append(int(num))
                    num = ''
    
        #print(res_list)
        re_list.append(res_list.copy())
        res_list.clear() # Обязательно очищать лист после каждого прохода, иначе будет наслоение данных.

    print(re_list)
    return re_list
    
# Цикл проверки достоверности

def proc_test(res_list):
    buff_list = [[1, 5], [1, 72]] # Список с правильными ответами [1, 5], [1, 5, 25], [1, 72]
    for elem in range(len(res_list)):
        if res_list[elem] == buff_list[elem]:
            print('Right answer:', buff_list[elem], 'Passed')
        else:
            print('Right answer:', res_list[elem], 'Not Passed', 'Your answer:', buff_list[elem])

# Запуск программы в целом

def main():
    res_list = main_proc()
    proc_test(res_list)

main()