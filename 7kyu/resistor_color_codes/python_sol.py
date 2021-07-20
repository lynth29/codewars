def decode_resistor_colors(bands):
    resistor_colors = {'black':0,
                       'brown':1,
                       'red':2,
                       'orange':3,
                       'yellow':4,
                       'green':5,
                       'blue':6,
                       'violet':7,
                       'gray':8,
                       'white':9,
                       'gold':5,
                       'silver':10}
    # Split bands into list
    bands = bands.split(' ')
    # Define ohms
    ohms = resistor_colors[bands[0]] * 10 + resistor_colors[bands[1]] * 10**resistor_colors[bands[2]]
    # Define tolerance
    tolerance = resistor_colors[bands[3]] if len(bands) > 3 else 20
    # Return result based on the amount of ohms
    if ohms < 1000:
        return f"{ohms} ohms, {tolerance}%"
    elif 1000 <= ohms < 1000000:
        return "{}k ohms, {}%".format(int(ohms/1000) if int(ohms/1000) == float(ohms/1000) else float(ohms/1000), tolerance)
    else:
        return "{}M ohms, {}%".format(int(ohms/1000000) if int(ohms/1000000) == float(ohms/1000000) else float(ohms/1000000), tolerance)
