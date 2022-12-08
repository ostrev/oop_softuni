class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            number = int(float_value)
            return cls(number)
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(len(value)):
            if i != len(value) - 1 and roman[value[i]] < roman[value[i + 1]]:
                num += roman[value[i]] * -1
            else:
                num += roman[value[i]]
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        try:
            return cls(int(value))
        except ValueError:
            return 'wrong type'




print(Integer.from_string('2.6'))
