N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
coins.reverse()

cnt = 0
won = 0
for coin in coins:
    cnt += (K-won) // coin
    won += ((K-won) // coin) * coin
    if K == won:
        break

print(cnt)
