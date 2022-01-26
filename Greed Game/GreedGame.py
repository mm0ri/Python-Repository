dice = [2,2,4,6,2]

def score(dice):
    DICE_DICT = {}
    d_score = 0
    for element in dice:
        DICE_DICT.update({element: dice.count(element)})

    for key,value in DICE_DICT.items():

        if key == 1 and value == 1:
            d_score = d_score + 100
        elif key == 1 and value == 3:
            d_score = d_score + 1000

        if key == 2 and value == 3:
            d_score = d_score + 200

        if key == 3 and value == 3:
            d_score = d_score + 300

        if key == 4 and value == 3:
            d_score = d_score + 400

        if key == 5 and value == 1:
            d_score = d_score + 50
        elif key == 5 and value == 3:
            d_score = d_score + 500

        if key == 6 and value == 3:
            d_score = d_score + 600

    #print(DICE_DICT, d_score)
    return d_score

score(dice)