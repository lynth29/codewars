def solution(string,markers):
    # Split string by \n
    lines = string.split('\n')
    # Run a for loop to go through each line
    for idx, line in enumerate(lines):
        # Run a for loop to find if marker is in line
        for marker in markers:
            # Find marker's index
            index = line.find(marker)
            # If the marker isn't in the last, reassign line
            if index != -1:
                line = line[:index]
        # Remove any white spaces at the end of the string and replace the old line in lines
        lines[idx] = line.rstrip(' ')
    # Join line by \n
    result = '\n'.join(lines)
    return result
