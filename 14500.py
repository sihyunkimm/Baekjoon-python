import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

shapes = [
    [[0, 0], [0, 1], [0, 2], [0, 3]], # -
    [[0, 0], [1, 0], [2, 0], [3, 0]], # |
    
    [[0, 0], [0, 1], [1, 0], [1, 1]], # ㅁ

    [[0, 0], [0, 1], [0, 2], [1, 1]], # ㅜ
    [[1, 0], [1, 1], [1, 2], [0, 1]], # ㅗ
    [[0, 1], [1, 1], [2, 1], [1, 0]], # ㅓ
    [[0, 0], [1, 0], [2, 0], [1, 1]], # ㅏ

    [[0, 0], [1, 0], [1, 1], [2, 1]], # N mirror
    [[1, 0], [1, 1], [0, 1], [0, 2]], # Z mirror

    [[0, 1], [1, 1], [1, 0], [2, 0]], # N
    [[0, 0], [0, 1], [1, 1], [1, 2]], # Z

    [[0, 0], [1, 0], [2, 0], [2, 1]], # L
    [[0, 0], [0, 1], [0, 2], [1, 0]], # 「
    [[0, 0], [0, 1], [1, 1], [2, 1]], # ㄱ
    [[1, 0], [1, 1], [1, 2], [0, 2]], # 」

    [[0, 1], [1, 1], [2, 1], [2, 0]], # L mirror 」
    [[0, 0], [1, 0], [1, 1], [1, 2]], # ㄴ
    [[0, 0], [1, 0], [2, 0], [0, 1]], # 「
    [[0, 0], [0, 1], [0, 2], [1, 2]]  # ㄱ
]


answer = 0
for r in range(N):
    for c in range(M):

        # r, c 위치에서 모든 도형 검사
        for shape in shapes:
            temp = 0
            isFit = True

            for p in shape:
                nr = r + p[0]
                nc = c + p[1]
                
                if not (0 <= nr < N and 0 <= nc < M):
                    isFit = False
                    break
                else:
                    temp += matrix[nr][nc]

            if isFit:
                answer = max(answer, temp)


print(answer)



def printShape():    
    for shape in shapes:
        pan = [[0 for _ in range(4)] for _ in range(4)]

        for p in shape:
            pan[p[0]][p[1]] = 1

        for i in pan:
            print(i)

        print()


