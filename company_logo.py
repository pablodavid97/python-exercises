from itertools import groupby

def company_logo(string):
    result = []

    for k, g in groupby(string):
        group_list = list(g)
        
        result.append([k, len(group_list)])

    sorted_result = sorted(result, key=lambda x: (-x[1], x[0]))

    for item in sorted_result:
        k, v = item
        print(f'{k} {v}')

def main():
    string_input = input()

    company_logo(string_input)

if __name__ == '__main__':
    main()