from itertools import groupby

def solution(args):
    # An empty list
    result = []
    # Group number by its range to the next number in list
    for idx, num in groupby(enumerate(args), lambda x: x[0] - x[1]):
        range_ = [x for _, x in num]
        if len(range_) > 2:
            result.append(f"{range_[0]}-{range_[-1]}")
        elif len(range_) == 1:
            result.append(f"{range_[0]}")
        else:
            result.append(f"{range_[0]},{range_[1]}")
    answer = ','.join(result)
    return answer
