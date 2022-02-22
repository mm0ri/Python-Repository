string = 'two hundred fifty five'
def parse_int():

    def hundred():
        pass
    def thousand():
        pass

    NUMBER_CODE = { 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 
                'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14', 'fiveteen':'15', 'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
                'twenty':'20', 'thirty':'30', 'fourty':'40', 'fifty':'50', 'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90', 'hundred':hundred(), 'thousand':thousand() }
                
    buff_list = string.split(' ')

    print(buff_list)
    #return

parse_int()