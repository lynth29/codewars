from itertools import combinations
def choose_best_sum(t, k, ls):
    combos = list(combinations(ls,k))
    sums = [sum(combo) for combo in combos]
    possible_answer = [sum for sum in sums if sum <= t]
    if len(possible_answer) == 0:
        return None
    else:
        return max(possible_answer)
