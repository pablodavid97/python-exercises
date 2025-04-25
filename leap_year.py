def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

    return leap

def main():
    year = int(input())

    if year < 1900 or year > 10**5:
        print('Invalid input!')
        return

    print(is_leap(year))


if __name__ == '__main__':
    main()