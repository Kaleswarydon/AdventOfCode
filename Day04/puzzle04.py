import pandas as pd
import re
import numpy as np
from functools import cache

def input_preparer(input_data: list):
    res = pd.DataFrame()
    for card in input_data:
        card_id = card[0].split(' ')[-1]
        card_numbers = [x for x in card[1].split(' ') if x]
        card_numbers_winning = [x for x in card[2].split(' ') if x]
        hits = list(set(card_numbers).intersection(set(card_numbers_winning)))
        #print(hits)
        score = np.power(2, len(hits) - 1) if len(hits) else 0
        entry = pd.DataFrame([{'card_id': card_id,
                    'card_numbers': ';'.join(card_numbers),
                    'card_numbers_winning': ';'.join(card_numbers_winning),
                    'hits': ';'.join(hits),
                    'score': score}])
        res = pd.concat([res, entry], ignore_index=True)
    return res



def get_won_cards(prep: pd.DataFrame):
    res = {}
    for i in prep.get('card_id'):
        won_numbers = [int(x) for x in list(prep.loc[prep['card_id'] == str(i), 'hits'])[0].split(';') if x]
        res.update({int(i): list(range(int(i) + 1, int(i) + 1 + len(won_numbers)))})
    return res

def puzzle2_solver_amount_only(prep2: dict):
    res = {}
    for k in prep2.keys():
        if res.get(k):
            res.update({k: res.get(k) + 1})
        else:
            res.update({k: 1})
        for w in prep2.get(k):
            if res.get(w):
                res.update({w: res.get(w) + res.get(k)})
            else:
                res.update({w: res.get(k)})
    return list(res.values())



if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()
        input_data = [[y.strip() for y in re.split(':|\|', x)] for x in input_data]
    prep = input_preparer(input_data)
    prep2 = get_won_cards(prep)
    #puzzle1
    puzzle1 = sum(prep.get('score'))
    print("puzzle1:", puzzle1)

    #puzzle2
    puzzle2 = sum(puzzle2_solver_amount_only(prep2))
    print("puzzle2:", puzzle2)