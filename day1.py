import re

def prob_1(f):
    total = 0
    for line in f:
        i = 1
        first_digit = None
        last_digit = None
        while not (first_digit and last_digit):
            if not first_digit and line[i - 1].isdigit():
                first_digit = line[i - 1]
            if not last_digit and line[-i].isdigit():
                last_digit = line[-i]
            
            if first_digit and last_digit:
                break
            i += 1
        total += (int(first_digit) * 10) + int(last_digit)
    print(f"Total: {total}")

def prob_2(f):
    # fxn to find the first digit, reverse the string, then find the first backwards digit
    possible_digits = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    reversed_digits = {k[::-1]: v for k, v in possible_digits.items()}
    regex = '|'.join(list(possible_digits.keys()))
    reverse_regex = '|'.join(list(reversed_digits.keys()))
    total = 0

    for line in f:
        first_digit = None
        last_digit = None
        word = ""

        # Get first digit
        for c in line:
            # c is a number
            if c.isdigit():
                first_digit = int(c)
                word = ""
                break
            
            # c is a char
            if c.isalpha():
                word += c
                match = re.search(regex, word)
                if match:
                    digit = possible_digits[match.group()]
                    first_digit = digit
                    word = ""
                    break
        
        # Get last digit
        for c in line[::-1]:
            if c.isdigit():
                last_digit = int(c)
                break
            if c.isalpha():
                word += c
                match = re.search(reverse_regex, word)
                if match:
                    digit = reversed_digits[match.group()]
                    last_digit = digit
                    break
                
        total += (first_digit * 10) + last_digit
        print(f"{line}{first_digit}{last_digit}")
    print(f"Total: {total}")
            

if __name__ == "__main__":
    # with open("test_input.txt", "r") as f:
    with open("day1_input.txt", "r") as f:
        # prob_1(f)
        prob_2(f)
