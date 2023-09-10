def knapsack_single(w, S):
    weight___is_possible = [not s % w for s in range(S + 1)]
    return weight___is_possible


#5 3 2, 10
#0 1 2 3 4 5 6 7 8 9 10
#1 0 0 0 0 1 0 0 0 0 1
#1 0 0 1 0 1 1 0 1 1 1
#1 0 1 1 1 1 1 1 1 1 1
def prefix_knapsack(weights, S):
    weights___is_possible = []
    for w in weights:
        if len(weights___is_possible) < 1:
            weights___is_possible.append(knapsack_single(w, S))
            continue
        weights___is_possible.append([False] * (S + 1) )
        for s in range(S + 1):
            weights___is_possible[-1][s] = weights___is_possible[-2][s] or weights___is_possible[-1][s - w]
    return weights___is_possible

def wrapper_preparation(weigths, S):
    return S - sum(weigths)

def wrapper_conclusion(valid_sets):
    return [[n + 1 for n in valid_set] for valid_set in valid_sets]

def calculate_divisions(weights, S):
    return [S // weight for weight in weights]

def backtracking_recursive(knapsack_results, weights, S):
    max_counts = calculate_divisions(weights, S)
    all_valid_sets = []

    def recursion(idx, curS, curCounts):
        if idx < 0:
            if curS != 0 or not knapsack_results[idx + 1][curS]:
                return
            all_valid_sets.append(curCounts[:])
            return

        if curS < 0 or not knapsack_results[idx][curS]:
            return

        for n in range(max_counts[idx] + 1):
            recursion(idx - 1, curS - weights[idx] * n, [n] + curCounts)

    recursion(len(weights) - 1, S, [])
    return all_valid_sets

