def palindromic_triange(n):
    for i in range(1, n+1): 
        print(*[a for a in range(1, i+1)] + [a for a in range(i-1, 0, -1)], sep='')

def main():
    n = int(input())

    palindromic_triange(n)

if __name__ == '__main__':
    main()