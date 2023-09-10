#0 1 2 3 4 5 6 7 8 9 10 -- S = 10
#0 0 0 0 0 1 0 0 0 0 2  -- 5
#0 0 0 0 0 0 0 1 0 2 0  -- 2
#0 0 0 0 0 0 0 0 0 0 1 -- 3
#idx < 0 and sum == 0
#1 0 0 0 0 1 0 0 0 0 1  -- 5
#1 0 1 0 1 1 1 1 1 1 1  -- 2
#1 0 1 1 1 1 1 1 1 1 1  -- 3
def knapsack(weights, S):
    min_multiplicities = []
    weights___is_possible = []
    capacities = range(S + 1)

    for w in weights:
        if len(min_multiplicities) < 1:
            min_multiplicities.append([s // w if s % w == 0 else 0 for s in capacities])
            weights___is_possible.append([not s % w for s in capacities])
            continue
        weights___is_possible.append([False] * (S + 1))
        min_multiplicities.append([0] * (S + 1))
        for s in capacities:
            weights___is_possible[-1][s] = weights___is_possible[-2][s] or weights___is_possible[-1][s - w]
            if not weights___is_possible[-1][s] or s < w:
                continue
            #If s - w could be reached by cur elem before, so +1
            multiplicity_1 = min_multiplicities[-1][s - w] + 1 if min_multiplicities[-1][s - w] > 0 else 0
            #If s - w could be reached using prev elems, so enough to take only one cur elem
            multiplicity_2 = 1 if min_multiplicities[-2][s - w] > 0 else 0
            #As valid sets should not contain 0, we try to take the min positive number
            if multiplicity_1 and multiplicity_2:
                min_multiplicities[-1][s] = min(multiplicity_1, multiplicity_2)
            elif multiplicity_1 != 0:
                min_multiplicities[-1][s] = multiplicity_1
            else:
                min_multiplicities[-1][s] = multiplicity_2

    return min_multiplicities

def backtracking(min_multiplicities, weigths, S):
    all_valid_sets = []

    def find_valid_sets(idx, cnt, s, cur_set):
        if s == 0 and idx == 0:
            all_valid_sets.append([cnt] + cur_set)
        if not min_multiplicities[idx][s]:
            return
        cur_min_mult = min_multiplicities[idx][s]
        if s - cur_min_mult * weigths[idx] > 0 and min_multiplicities[idx][s - cur_min_mult * weigths[idx]] or idx == 0 and s - cur_min_mult * weigths[idx] == 0:
            find_valid_sets(idx, cnt + cur_min_mult, s - cur_min_mult * weigths[idx], cur_set)
        if s - cur_min_mult * weigths[idx] >= 0 and idx > 0 and min_multiplicities[idx - 1][s - cur_min_mult * weigths[idx]]:
            find_valid_sets(idx - 1, 0, s - cur_min_mult * weigths[idx], [cnt + cur_min_mult] + cur_set)

    find_valid_sets(len(weigths) - 1, 0, S, [])
    return all_valid_sets

def find_multiplicities(weigths, S):
    min_multiplicities = knapsack(weigths, S)
    return backtracking(min_multiplicities, weigths, S)