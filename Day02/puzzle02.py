
def get_draws(g: str):
    res = {'game_id': 0, 'draws': []}
    tmp = [x.strip() for x in g.split(':')]
    res.update({'game_id': int(tmp[0].split(' ')[1])})
    draws = [x.strip() for x in tmp[1].split(';')]
    for d in draws:
        tmp_draw_list = res.get('draws')
        colors = [x.strip() for x in d.split(',')]
        tmp_draw = {}
        for c in colors:
            tmp2 = c.split(' ')
            color = tmp2[1]
            amount = tmp2[0]
            tmp_draw.update({color: int(amount)})
            tmp_draw_list.append(tmp_draw)
        res.update({'draws': tmp_draw_list})
    return res

def is_valid_game(game: dict, condition: dict):
    min_config = {'red': 0, 'green': 0, 'blue': 0}
    for d in game.get('draws'):
        for c in d.keys():
            if min_config.get(c) < d.get(c):
                min_config.update({c: d.get(c)})
    for c in min_config.keys():
        if condition.get(c) < min_config.get(c):
            return False, min_config
    return True, min_config

def check_game_batch_validity(games: list, condition: dict):
    res_valid = {}
    res_invalid = {}
    for game in games:
        draws = get_draws(game)
        is_valid, min_config = is_valid_game(draws, condition)
        if is_valid:
            res_valid.update({draws.get('game_id'): min_config})
        else:
            res_invalid.update({draws.get('game_id'): min_config})
    return res_valid, res_invalid

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()

    #puzzle1
    condition1 = {'red': 12, 'green': 13, 'blue': 14}
    res1_valid, res1_invalid = check_game_batch_validity(input_data, condition1)
    #add ids of possible games together
    puzzle1 = sum(res1_valid.keys())
    print('puzzle1:', puzzle1)

    #puzzle2
    powers = []
    res1_combined = {}
    res1_combined.update(res1_valid)
    res1_combined.update(res1_invalid)
    for r in res1_combined:
        tmp = 1
        for p in res1_combined.get(r).values():
            tmp *= p
        powers.append(tmp)
    print('puzzle2:', sum(powers))
