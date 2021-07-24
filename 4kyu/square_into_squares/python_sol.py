def decompose(n):
    total = 0
    # Adding n to answer list
    answer = [n]
    while answer:
        temp = answer.pop()
        # Removing n from list and adding it to total
        total += temp ** 2
        # Run a for loop from the least number below total to 1
        for i in range(temp - 1, 0, -1):
            # If it's within the range, adding to answer list
            # and subtracting from total
            if total - (i**2) < 0:
                pass
            else:
                total -= i**2
                answer.append(i)
                # When total reach 0, return answer list
                if total == 0:
                    return(sorted(answer))
    else:
        return None
## Timeout
decompose(1000000)
