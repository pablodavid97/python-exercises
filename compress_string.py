from itertools import groupby

def compress_string(string):
    result = []

    for k, g in groupby(string):
        group_list = list(g)

        result.append((len(group_list), k))

    print(result)

def main():
    string_input = input()

    compress_string(string_input)


if __name__ == '__main__':
    main()