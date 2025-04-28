from collections import deque

def piling_up(blocks, n):
    blocks_deque = deque(blocks)
    prev_cube = float('inf')

    while blocks_deque:
        left = blocks_deque[0]
        right = blocks_deque[-1]

        if left >= right:
            current = left
            blocks_deque.popleft()
        else:
            current = right
            blocks_deque.pop()

        if current > prev_cube:
            return 'No'

        prev_cube = current

    return 'Yes'

def main():
    T = int(input())

    for i in range(0, T):
        n = int(input())
        block_list = list(map(int, input().split()))

        print(piling_up(block_list, n))

if __name__ == '__main__':
    main()