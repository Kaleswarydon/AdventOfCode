import pandas as pd
import itertools

def make_max_hand(h): #if hand has jokers, make max valuable hand out of it
    possible_chars = [x for x in list(set(list(h))) if x != 'J']
    if not possible_chars:
        possible_chars = ['A']
    possible_combinations = [p for p in itertools.product(possible_chars, repeat=h.count('J'))]
    joker_indices = [i for i, c in enumerate(h) if c == 'J']
    tmp = set()
    for combination in possible_combinations:
        hand = list(h)
        for ind, ji in enumerate(joker_indices):
            hand[ji] = combination[ind]
            tmp.add(''.join(hand))
    res = ['', '', 0, 0] # hand, category_text, category, value (sum)
    for per in tmp:
        cat, cat_text = categorize_hand(per)
        val = float(str(int(get_card_val_hex(str(cat) + per), 16)))
        #print([per, cat_text, cat, val])
        if not res[0] or int(cat) > int(res[2]) and int(val) > int(res[3]):
            res = [per, cat_text, cat, val]
    return res

def categorize_hand(h):
    amount_dict = {}
    for x in h:
        if amount_dict.get(x):
            amount_dict.update({x: amount_dict.get(x) + 1})
        else:
            amount_dict.update({x: 1})
    vals = amount_dict.values()
    if 5 in vals:  # five of a kind
        return 6, 'five_of_a_kind'
    elif 4 in vals:  # four of a kind
        return 5, 'four_of_a_kind'
    elif 3 in vals:
        if 2 in vals:  # full house
            return 4, 'full_house'
        else:  # three of a kind
            return 3, 'three_of_a_kind'
    elif 2 in vals:
        if len(vals) == 3:  # two pair
            return 2, 'two_pair'
        else:  # one pair
            return 1, 'one_pair'
    else:  # high card
        return 0, 'high_card'

def compare_hands(h1, h2):
    for i, x in enumerate(h1):
        comp = card_compare(h1[i], h2[i])
        if comp:
            return 0 if comp > 0 else 1 #0 if h1 is superior, 1 else
    return -1 #if both hands are the same
def card_compare(c1, c2):
    return get_card_val(c1) - get_card_val(c2)

def get_card_val(c, option=1):
    if option == 1:
        card_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    else:
        card_dict = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
    if not card_dict.get(c):
        ret = 0
        try:
            ret = int(c)
        except:
            pass
        return ret
    return card_dict.get(c)


def get_card_val_hex(c, option=1):
    #print(c)
    res = ''
    for x in c:
        #print(hex(get_card_val(x)))
        res += hex(get_card_val(x, option)).split('x')[-1]
    return res

def input_prep(input_data):
    input_data_dataframe = pd.DataFrame()
    for x in input_data:
        if len(x) == 5 and x[4]:
            cat = x[4]
            cat_text = x[3]
            option = 2
        else:
            cat, cat_text = categorize_hand(x[0])
            option = 1
        hex_val_cat = get_card_val_hex(str(cat) + x[0], option)
        tmp_frame = pd.DataFrame([{'hand': x[0],
                                   'bid': int(x[1]),
                                   'category': cat,
                                   'category_text': cat_text,
                                   'hex_val_cat': hex_val_cat,
                                   'dec_val_cat': float(str(int(hex_val_cat, 16)))}])
        input_data_dataframe = pd.concat([input_data_dataframe, tmp_frame], ignore_index=True)
    input_data_dataframe = input_data_dataframe.sort_values(by=['dec_val_cat']).reset_index(drop=True)
    input_data_dataframe['rank'] = input_data_dataframe.index + 1
    return input_data_dataframe

def input_pre_prep(input_data):
    res = []
    for h in input_data:
        max_hand = make_max_hand(h[0])
        #print(max_hand)
        res.append([h[0], h[1], max_hand[0], max_hand[1], max_hand[2]])
    return res

def puzzle_solver(prep):
    res = 0
    for i in prep.index:
        res += prep.iloc[i]['rank'] * prep.iloc[i]['bid']
    return res

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = [x.split() for x in f.readlines()]
    prep1 = input_prep(input_data)
    #print(prep1)
    # puzzle1
    print('puzzle1:', puzzle_solver(prep1))

    # puzzle2
    #make_max_hand('AJJA5')
    input_data = input_pre_prep(input_data)
    #print(input_data)
    prep2 = input_prep(input_data)
    #print(prep2)
    print('puzzle2:', puzzle_solver(prep2))

