from heapq import heappop, heappush

n = int(input())
lines = sorted([sorted(list(map(int,input().split()))) for _ in range(n)], key=lambda x: x[1]) # 끝점 기준 오름차순
d = int(input())

answer = 0
heap = []
# 끝점 오름차순 순서로 진행
for s, e in lines:

    # 출퇴근 길이가 더 길면 패스
    if e - s > d:
        continue

    # 현재 끝점에서 노선 길이만큼 뺀 값보다 시작점이 더 작은 곳에 있는 사람 힙에서 제거
    while heap and heap[0][0] < e - d:
        heappop(heap)
        
    # 현재 사람 힙에 추가
    heappush(heap, (s, e))

    # 힙 개수 최댓값 저장
    answer = max(answer,len(heap))

print(answer)