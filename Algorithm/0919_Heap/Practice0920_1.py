import sys
sys.stdin = open("../input.txt", "r")
# 최소, 최대 힙 사용할 예정
import heapq

N = int(input())

# 초기값 설정
mid = 500
right_heap = []
left_heap = []

for n in range(N):
    # 성적 입력
    scores = list(map(int, input().split()))
    for score in scores:  # 성적을 양쪽 힙에 조건에 맞게 추가
        if score <= mid:  # 중앙값보다 성적이 낮다면 왼쪽
            heapq.heappush(left_heap, -score)  # 최대힙 구현을 위해 음수로 입력
        else:             # 중앙값보다 성적이 높다면 오른쪽
            heapq.heappush(right_heap, score)

    # 중앙값 수정
    len_left = len(left_heap)
    len_right = len(right_heap)
    # 왼쪽 힙에 둘이 들어갔다면, 중앙값을 오른쪽에 넣고 왼쪽힙의 최댓값을 중앙값으로 수정
    if len_left < len_right:
        heapq.heappush(left_heap, -mid)
        mid = heapq.heappop(right_heap)
    # 오른쪽 힙에 둘이 들어갔다면, 중앙값을 왼쪽에 넣고 오른쪽힙의 최댓값을 중앙값으로 수정
    elif len_left > len_right:
        heapq.heappush(right_heap, mid)
        mid = -heapq.heappop(left_heap)
    # 수정된 중앙값 출력, 양쪽에 하나씩 들어갔다면 연산없이 이전값이 출력됨
    print(mid)