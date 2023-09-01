import sys
sys.stdin = open("input.txt", "r")


def combination(i, n):



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

arr.sort(key = lambda x: (x[1], x[0]))

print(result)