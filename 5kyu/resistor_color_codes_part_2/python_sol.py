resistor_colors = {0:'black', 1:'brown', 2:'red', 3:'orange', 4:'yellow', 5:'green', 6:'blue', 7:'violet', 8:'gray', 9:'white'}

def encode_resistor_colors_1(ohms_string):
    ohms_string = ohms_string.split(' ')
    ohms = []
    if ohms_string[0][-1] not in 'kM':
        for i in ohms_string[0][:2]:
            ohms.append(resistor_colors[int(i)])
        ohms.append('brown' if len(ohms_string[0]) == 3 else 'black')
    else:
        multiply = 1000 if ohms_string[0][-1] == 'k' else 1000000
        ori_num = float(ohms_string[0][:-1]) * multiply
        for i in str(ori_num)[:2]:
            ohms.append(resistor_colors[int(i)])
        ohms.append(resistor_colors[len(str(ori_num)[2:-2])])
    ohms.append('gold')
    return " ".join(ohms)


# Better solution
def encode_resistor_colors(ohms_string):
    ohms_string = ohms_string.replace(' ohms','').replace('k','*1000').replace('M','*1000000')
    ohms_string = str(int(eval(ohms_string)))
    return f"{resistor_colors[int(ohms_string[0])]} {resistor_colors[int(ohms_string[1])]} {resistor_colors[len(ohms_string[2:])]} gold"
