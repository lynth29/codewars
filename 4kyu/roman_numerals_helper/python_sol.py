class RomanNumerals:

    @classmethod
    def to_roman(self, value):
        self.roman = ''
        if value >= 1000:
            (div, value) = divmod(value, 1000)
            self.roman += 'M' * div
        if value >= 100:
            (div, value) = divmod(value, 100)
            if div == 9:
                self.roman += 'CM'
            elif div >= 5:
                self.roman += 'D' + 'C' * (div-5)
            elif div == 4:
                self.roman += 'CD'
            else:
                self.roman += 'C' * div
        if value >= 10:
            (div, value) = divmod(value, 10)
            if div == 9:
                self.roman += 'XC'
            elif div >= 5:
                selfroman += 'L' + 'X' * (div-5)
            elif div == 4:
                self.roman += 'XL'
            else:
                self.roman += 'X' * div
        if value == 9:
            self.roman += 'IX'
        elif value >= 5:
            self.roman += 'V' + 'I' * (value-5)
        elif value == 4:
            self.roman += 'IV'
        else:
            self.roman += 'I' * value
        return self.roman

    @classmethod
    def from_roman(self, string):
        to_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.value = 0
        lst = []
        for word in string:
            lst.append(to_dict[word])
        self.value += lst[-1]
        if len(lst) > 1:
            for i in range(len(lst) - 2, 0, -1):
                if lst[i] < lst[i+1]:
                    self.value -= lst[i]
                else:
                    self.value += lst[i]
            if lst[0] < lst[1]:
                self.value -= lst[0]
            else:
                self.value += lst[0]
        return self.value
