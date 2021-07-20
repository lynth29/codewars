import re

def phone(strng, num):
    if num not in strng:
        return f"Error => Not found: {num}"
    if num in strng:
        if strng.count(num) > 1:
            return f"Error => Too many people: {num}"
        else:
            lst = strng.split('\n')
            for i in lst:
                if num in i:
                    # Find name
                    start_name = i.find("<")
                    end_name = i.find(">")
                    name = i[start_name+1:end_name]
                    # Find address
                    address = i.replace(name,"").replace(num,"")
                    address = re.sub("[^.\-\w\s]","", address).strip()
                    address = re.sub("  |[_]"," ", address).strip()
                    return f"Phone => {num}, Name => {name}, Address => {address}"
