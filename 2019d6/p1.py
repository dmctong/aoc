from collections import deque
from collections import defaultdict

filename = 'e.txt'

graph = defaultdict(list)
with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(')')
        graph[line[0]].append(line[1])

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
    orbits += len(*all_paths[value])-1

print(f'Part 1: there are {orbits} direct and indirect orbits.')