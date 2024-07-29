import sys
n = int(input())
have = list(map(int, sys.stdin.readline().split()))
haveDic = {have[i]: i for i in range(n)}
m = int(input())
guess = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if guess[i] in haveDic:
        print(1, end=' ')
    else:
        print(0, end=' ')
