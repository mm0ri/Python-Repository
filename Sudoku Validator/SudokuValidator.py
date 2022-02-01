board =[[1, 3, 2, 5, 7, 9, 4, 6, 8], 
        [4, 9, 8, 2, 6, 1, 3, 7, 5], 
        [7, 5, 6, 3, 8, 4, 2, 1, 9], 
        [6, 4, 3, 1, 5, 8, 7, 9, 2], 
        [5, 2, 1, 7, 9, 3, 8, 4, 6], 
        [9, 8, 7, 4, 2, 6, 5, 3, 1], 
        [2, 1, 4, 9, 3, 5, 6, 8, 7], 
        [3, 6, 5, 8, 1, 7, 9, 2, 4], 
        [8, 7, 9, 6, 4, 2, 1, 3, 5]]

def valid_solution(board):
        flag = 0
        for row in board:
                #print("-----")
                for elem in row:
                        count_res = row.count(elem)
                        if count_res > 1:
                                flag = 1
                        print("elem", elem)
                        print("count", row.count(elem))
        if flag == 1:
                print("False")
                return False
        else:
                print("True")
                return True

valid_solution(board)