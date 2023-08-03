# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다.
# 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
#
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )
"""
3
3 6
5 15
5 10
"""
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""
#1 1
#2 1
#3 0
"""

import sys
sys.stdin = open("input.txt", "r")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())


def combination(N, K):
    result = 0
    j = 0
    for _ in range(13-N):
        nums = []
        for i in range(j, 12):
            if len(nums) < N:
                nums.append(A[i])
            elif sum(nums) != K:
                nums.pop()
                nums.append(A[i])
            elif len(nums) == N and sum(nums) == K:
                result += 1
                nums.pop()
                nums.append(A[i])
        j += 1

    return result


for tc in range(1, T+1):
    n, k = map(int, input().split())
    print(f'#{tc} {combination(n, k)}')

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# T = int(input())
#
#
# def count_subsets_with_sum(N, K, index, current_sum):
#     if N == 0:
#         return 1 if current_sum == K else 0
#
#     if index >= len(A):
#         return 0
#
#     # 현재 원소를 선택하는 경우
#     count_with_current = count_subsets_with_sum(N - 1, K, index + 1, current_sum + A[index])
#
#     # 현재 원소를 선택하지 않는 경우
#     count_without_current = count_subsets_with_sum(N, K, index + 1, current_sum)
#
#     return count_with_current + count_without_current
#
#
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     count = count_subsets_with_sum(N, K, 0, 0)
#     print(f'#{tc} {count}')
