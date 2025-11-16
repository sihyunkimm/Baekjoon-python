import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
NULL = -1

testcase = int(input())

for _ in range(testcase):
    num_building, num_rule = map(int, input().split())
    build_times = [0]
    build_times.extend(map(int, input().split()))
    
    r_graph = [[] for _ in range(num_building + 1)]
    for _ in range(num_rule):
        s, e = map(int, input().split())
        r_graph[e].append(s)    
    
    to_build = int(input())
    total_times = [NULL for _ in range(num_building + 1)]
    
    def time_to_build(building):
        if total_times[building] != NULL:
            return total_times[building]
        
        if not r_graph[building]:
            total_times[building] = build_times[building]
            return build_times[building]
        
        max_time = 0
        for prev in r_graph[building]:
            max_time = max(max_time, time_to_build(prev))

        total_times[building] = max_time + build_times[building]
        return max_time + build_times[building]
    
    print(time_to_build(to_build))