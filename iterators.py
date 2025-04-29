from itertools import combinations

def probability_calculator(list_input, n, k):
    touple_list = list(combinations(range(1, n+1), k))
    a_indexes = [i + 1 for i, val in enumerate(list_input) if val == 'a']

    ocurrence_count = sum(1 for tup in touple_list if any(elem in a_indexes for elem in tup))

    probability = ocurrence_count / len(touple_list)

    return round(probability, 3)

def main():
    n = int(input())
    list_input = input().split()
    k = int(input())

    print(probability_calculator(list_input, n, k))

if __name__ == '__main__':
    main()