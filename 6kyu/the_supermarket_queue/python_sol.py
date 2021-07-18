def queue_time(customers, n: int):
    # Create a list of tills, imagine each element is a till
    tills = [0]*n
    # Run a for loop to go through each customers
    for i in customers:
        # And each i customer go to a till
        tills[0] += i
        # Sort the tills again so the till that is fastly available become first
        # So when we assign an i customer again it comes to that available till
        tills.sort()
    return max(tills)
