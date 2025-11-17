from heapq import *
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    minHeap = []
    maxHeap = []
    maxDeleteQueue = {}
    minDeleteQueue = {}
    len = 0
    k = int(input())

    for _ in range(k):
        command, value = input().split()
        value = int(value)

        if command == 'I':
            heappush(minHeap, value)
            heappush(maxHeap, -value)
            len += 1

        elif command == 'D' and value == 1:
            while maxHeap and maxHeap[0] in maxDeleteQueue and maxDeleteQueue[maxHeap[0]] > 0:
                maxDeleteQueue[maxHeap[0]] -= 1
                heappop(maxHeap)

            if len == 0:
                continue

            key = -heappop(maxHeap)
            if key in minDeleteQueue:
                minDeleteQueue[key] += 1
            else:
                minDeleteQueue[key] = 1

            len -= 1

        else:
            while minHeap and minHeap[0] in minDeleteQueue and minDeleteQueue[minHeap[0]] > 0:
                minDeleteQueue[minHeap[0]] -= 1
                heappop(minHeap)

            if len == 0:
                continue

            key = -heappop(minHeap)
            if key in maxDeleteQueue:
                maxDeleteQueue[key] += 1
            else:
                maxDeleteQueue[key] = 1

            len -= 1


    while maxHeap and maxHeap[0] in maxDeleteQueue and maxDeleteQueue[maxHeap[0]] > 0:
        maxDeleteQueue[maxHeap[0]] -= 1
        heappop(maxHeap)
    while minHeap and minHeap[0] in minDeleteQueue and minDeleteQueue[minHeap[0]] > 0:
        minDeleteQueue[minHeap[0]] -= 1
        heappop(minHeap)

    if len == 0:
        print("EMPTY")
    else:
        print(-maxHeap[0], minHeap[0])
