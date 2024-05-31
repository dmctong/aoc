from collections import deque
from collections import defaultdict
from itertools import chain

filename = 'e.txt'
filename = 'e2.txt'

graph = defaultdict(list)
# all_nodes = set()
with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(')')
        graph[line[0]].append(line[1])
        # all_nodes.add(int(line[0]))

# print(graph)
# print(all_nodes)

def dfs(graph, start):
    all_paths = defaultdict(list)
    queue = deque()
    queue.append([start])

    while queue:
        path = queue.pop()
        s = path[-1]

        all_paths[s].append(path)

        for n in graph[s]:
            copy_path = path[:]
            copy_path.append(n)
            queue.append(copy_path)
    
    return(all_paths)

all_paths = dfs(graph, 'COM')
orbits = 0
for key, value in enumerate(all_paths):
    # print(key)
    # print(value)
    orbits += len(*all_paths[value])-1
    # print(*all_paths[value])

print(f'Part 1: there are {orbits} direct and indirect orbits.')

print(graph)

def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()
    visited.add(start)

    while queue:
        path = queue.popleft()
        s = path[-1]

        if s == end:
            final_path = path
            break
        for n in graph[s]:
            copy_path = path[:]
            copy_path.append(n)
            queue.append(copy_path)
            visited.add(n)
    return(final_path)

print(bfs(graph, 'YOU', 'SAN'))
