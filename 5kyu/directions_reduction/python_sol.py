def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    dir = []
    for direction in arr:
        if dir and dict[direction] == dir[-1]:
            print(direction, dir)
            dir.pop()
        else:
            print(dir)
            dir.append(direction)
            print(direction, dir)
    return dir
