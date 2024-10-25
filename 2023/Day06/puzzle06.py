import math

def win_calc(timedist_list):
    t = int(timedist_list[0])
    d = int(timedist_list[1])
    for x in range(math.ceil(t / 2)):
        tmp_d = x * (t - x)
        if tmp_d > d:
            return t - (x * 2) + 1 # +1 because we start at 0 which is not counted by loop

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = [x.split()[1:] for x in f.readlines()]

    #puzzle1
    win_press_times1 = [win_calc([input_data[0][r], input_data[1][r]]) for r in range(len(input_data[0]))]
    print('puzzle1:', math.prod(win_press_times1))

    #puzzle2
    win_press_times2 = win_calc([''.join(x) for x in input_data])
    print('puzzle2:', win_press_times2)
