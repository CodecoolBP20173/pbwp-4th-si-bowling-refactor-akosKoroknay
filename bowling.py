def score(game):
    result = 0
    frame = 1
    first_try = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i + 1])
            elif game[i].lower() == 'x':
                result += get_value(game[i + 1])
                if game[i + 2] == '/':
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        if not first_try or game[i].lower() == 'x':
            frame += 1
            first_try = True
        else:
            first_try =  False
    return result


def get_value(char):
    values = {'1': 1, '2': 2, '3': 3, '4': 4,\
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'x': 10,\
    '/': 10, '-': 0}
    if char.lower() in values:
        return values[char.lower()]
    else:
        raise ValueError()
    