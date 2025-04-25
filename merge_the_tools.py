def merge_the_tools(string, k):
    n = len(string)
    t = [string[i:i + k] for i in range(0, n, k)]
    u = []

    for i in range(0, len(t)):
        substring = t[i]
        u_item = ''

        for j in range(0, len(substring)):
            if substring[j] not in u_item:
                u_item += substring[j]
        
        u.append(u_item)

    for i in range(0, len(u)):
        print(u[i])


def main():
    string_input = input()
    k_input = int(input())
    n = len(string_input)

    if n < 1 or n > 10**4:
        print('Invalid input!')
        return
    elif k_input < 1 or k_input > n:
        print('Invalid input!')
        return
    elif n % k_input != 0:
        print('Invalid input!')
        return

    merge_the_tools(string_input, k_input)

if __name__ == '__main__':
    main()