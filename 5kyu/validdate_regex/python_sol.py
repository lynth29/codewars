import re
days28 = "02-(0[1-9]|1\d|2[0-8])"
days30 = "(?:0[469]|11)-(?:0[1-9]|[12]\d|30)"
days31 = "(?:0[13578]|10|12)-(?:0[1-9]|[12]\d|3[01])"

valid_date = re.compile(rf"\[+((?:{days28})|(?:{days30})|(?:{days31}))+\]")