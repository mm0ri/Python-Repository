string = 'two hundred fifty five'
def parse_int():
    buff_list = string.split(' ')
    res_list = []

    var = 2
    def hundred(var):
        var = str(var*100)
        return var
    def thousand(var):
        var = str(var*1000)
        return var

    NUMBER_CODE = { 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 
                'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fiveteen':'15', 'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
                'twenty':'20', 'thirty':'30', 'fourty':'40', 'fifty':'50', 'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90', 'hundred':hundred(var), 'thousand':thousand(var) }

    for element in buff_list:
        if element == 'hundred':
            res_list.append(buff_list[element-1] * 100)
        if element == 'thousand':
            res_list.append(buff_list[element-1] * 1000)


    print(res_list)
    #return

parse_int()