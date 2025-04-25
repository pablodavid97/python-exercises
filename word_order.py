def word_order(n, word_list):
    distinct_words = {}

    for i in range(0, n):
        if word_list[i] not in distinct_words:
            distinct_words[word_list[i]] = 1
        else:
            distinct_words[word_list[i]] += 1
    
    print(len(distinct_words))
    print(list(distinct_words.values()))

def main():
    n = int(input())
    word_list = []

    for i in range(0, n):
        word = input()
        word_list.append(word)

    word_order(n, word_list)

if __name__ == '__main__':
    main()