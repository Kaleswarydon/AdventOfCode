import re

def input_prep(l: list):
    return [x.strip() for x in l]

def input_prep2(l: list):
    word_to_number = {'one': '1',
                       'two': '2',
                       'three': '3',
                       'four': '4',
                       'five': '5',
                       'six': '6',
                       'seven': '7',
                       'eight': '8',
                       'nine': '9'}
    res = []
    for d in l:
        temp = d
        minmax = {}
        for n in word_to_number.keys():
            for z in range(len(temp)):
                if temp.find(n, z) != -1:
                    minmax.update({temp.find(n, z): word_to_number.get(n)})
        if minmax:
            maxpos = max(minmax.keys())
            minpos = min(minmax.keys())
            temp = temp[:minpos] + str(minmax.get(minpos)) + temp[minpos:]
            if len(minmax) > 1:
                temp = temp[:maxpos + 1] + str(minmax.get(maxpos)) + temp[maxpos + 1:]
        res.append(temp)
    return res

def solver(input_data: list):
    result = 0
    for x in input_data:
        temp_digits = []
        for y in x:
            try:
                temp_digits.append(int(y))
            except:
                pass
        try:
            result += int(str(temp_digits[0]) + str(temp_digits[-1]))
        except:
            pass
    return result

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()

    input_data_1 = input_prep(input_data)
    input_data_2 = input_prep2(input_data_1)

    #puzzle 1
    puzzle1 = solver(input_data_1)
    print("puzzle1:", puzzle1)

    #puzzle2
    puzzle2 = solver(input_data_2)
    print("puzzle2:", puzzle2)