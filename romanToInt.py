
def romanToInt_my_code(s:str):
    symbols = {
        'I': 1,
        'V':5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    letter_trans_toint_list = []
    for i in s:
        for sym in symbols:
            if sym == i:
                letter_trans_toint_list.append(symbols[sym])
    step1 = []
    step2 = []
    for num in range(len(letter_trans_toint_list)):
        if len(letter_trans_toint_list) > 1:
            if num == 0:
                current = letter_trans_toint_list[num]
                next = letter_trans_toint_list[num + 1]
                if current < next:
                    real_num = letter_trans_toint_list[num + 1] - letter_trans_toint_list[num]
                    step1.append(real_num)
                else:
                    step1.append(letter_trans_toint_list[num])
            elif num < len(letter_trans_toint_list) - 1:
                current = letter_trans_toint_list[num]
                next = letter_trans_toint_list[num + 1]
                if current < next:
                    real_num = letter_trans_toint_list[num + 1] - letter_trans_toint_list[num]
                    if step1[-1] >= real_num:
                        step1.append(real_num)
                elif current >= next:
                    if step1[-1] >= current:
                        step1.append(current)
            elif num == len(letter_trans_toint_list) - 1:
                last = letter_trans_toint_list[num]
                if step1[-1] >= last:
                    step1.append(last)
        else:
            current = letter_trans_toint_list[num]
            step1.append(current)

    return sum(step1)


def romanToInt_best_runtime(s:str):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


def romanToInt_best_memory_saving(s: str):
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    i = 0
    while i < len(s):
        if i != len(s) - 1:
            if (s[i], s[i + 1]) in ([
                ('I', 'V'), ('I', 'X'),
                ('X', 'L'), ('X', 'C'),
                ('C', 'D'), ('C', 'M')
            ]):
                num += m[s[i + 1]] - m[s[i]]
                i += 2
                continue
        num += m[s[i]]
        i += 1

    return num


if __name__ == "__main__":
    #s = 'MCMXCIV'
    #s = "LVIII"
    #s = "IV"
    s = "D"
    my_result = romanToInt_my_code(s)
    best_runtime = romanToInt_best_runtime(s)
    best_memory_saving = romanToInt_best_memory_saving(s)
    print(my_result)
    print(best_runtime)
    print(best_memory_saving)