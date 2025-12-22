N = int(input())

MIN = 0
MAX = 1
LEFT = 0
MID = 1
RIGHT = 2

for i in range(N):
    numbers = list(map(int, input().split()))
    temp = [[numbers[LEFT],numbers[LEFT]], [numbers[MID],numbers[MID]], [numbers[RIGHT],numbers[RIGHT]]] # [min, max]
    
    if i == 0:
        prev = temp
        continue

    temp[LEFT] = [numbers[LEFT] + min(prev[LEFT][MIN], prev[MID][MIN]), 
                   numbers[LEFT] + max(prev[LEFT][MAX], prev[MID][MAX])]
    temp[MID] = [numbers[MID] + min(prev[LEFT][MIN], prev[MID][MIN], prev[RIGHT][MIN]), 
                  numbers[MID] + max(prev[LEFT][MAX], prev[MID][MAX], prev[RIGHT][MAX])]
    temp[RIGHT] = [numbers[RIGHT] + min(prev[MID][MIN], prev[RIGHT][MIN]), 
                    numbers[RIGHT] + max(prev[MID][MAX], prev[RIGHT][MAX])]
    prev = temp

print(max(prev[LEFT][MAX], prev[MID][MAX], prev[RIGHT][MAX]), 
      min(prev[LEFT][MIN], prev[MID][MIN], prev[RIGHT][MIN]))