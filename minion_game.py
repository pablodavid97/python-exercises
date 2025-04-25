def minion_game(string):
    stuart = 0
    kevin = 0

    vowels = 'AEIOU'
    kevin_substrings = []
    stuart_substrings = []

    for i in range(len(string)):
        if string[i] in vowels:
            for j in range(i + 1, len(string) + 1):
                kevin_substrings.append(string[i:j])
        else:
            for j in range(i + 1, len(string) + 1):
                stuart_substrings.append(string[i:j])

    kevin = len(kevin_substrings)
    stuart = len(stuart_substrings)

    if (kevin > stuart):
        print('Kevin: ', kevin)
    else:
        print('Stuart: ', stuart)


def main():
    string = input()

    if len(string) <= 0 or len(string) > 10**6:
        print('Invalid input')
        return
    elif any(char.islower() for char in string):
        print('Invalid input')
        return
    elif any(not char.isalpha() for char in string):
        print('Invalid input')
        return

    minion_game(string)


if __name__ == '__main__':
    main()