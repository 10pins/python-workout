### Exercise 4 - Hexadeciamal output ###

def hex_output(hex):
    base_10 = 0
    max_pow = len(hex) - 1

    for index,digit in enumerate(hex):
        pow = max_pow - index
        base_10 += int(digit,16) * 16**pow

    return base_10

if __name__ == "__main__":
    print(hex_output('A0'))

