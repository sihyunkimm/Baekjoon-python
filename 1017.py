N = int(input())
numList = list(map(int, input().split()))
firstNum = numList[0]
numList.sort()

primeList = [2]

maxSum = numList[-1] + numList[-2]
for n in range(3, maxSum + 1):
    i = 0
    isNPrime = True
    while i < len(primeList) and primeList[i] <= n**0.5:
        if n % primeList[i] == 0:
            isNPrime = False
        i += 1
    if isNPrime:
        primeList.append(n)

primeSet = set(primeList)

answers = []

def canMatch(numbers, primeSet):
    n = len(numbers)
    if n % 2 != 0 or n == 0:
        return False
    
    odd = [i for i in range(n) if numbers[i] % 2 == 1]
    even = [i for i in range(n) if numbers[i] % 2 == 0]
    
    if len(odd) != len(even):
        return False    
    
    adj = [[] for _ in range(n)]
    for i in odd:
        for j in even:
            if numbers[i] + numbers[j] in primeSet:
                adj[i].append(j)
    
    # odd left, even right
    matchEven = [-1] * n
    matchOdd = [-1] * n
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if matchEven[v] == -1 or dfs(matchEven[v], visited):
                matchEven[v] = u
                matchOdd[u] = v
                return True
        return False
    
    # 모든 odd 노드가 매칭되는지 확인
    for u in odd:
        visited = [False] * n
        if not dfs(u, visited):
            return False
    
    return True


for i in numList:
    if i == firstNum: 
        continue

    if firstNum + i in primeSet:
        if N == 2:
            answers.append(i)
            break

        newNumList = [x for x in numList]
        newNumList.remove(firstNum)
        newNumList.remove(i)
        
        if N != 2 and canMatch(newNumList, primeSet):
            answers.append(i)

if not answers:
    answers.append(-1)

answers = list(set(answers))
answers.sort()

print(*answers)