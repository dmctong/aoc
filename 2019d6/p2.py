from collections import deque
from collections import defaultdict

filename = 'e.txt'
filename = 'e2.txt'
filename = 'i.txt'

graph = defaultdict(list)
with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split(')')
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])


def dfs(graph, start, end):
    queue = deque()
    queue.append([start])

    while queue:
        path = queue.pop()
        s = path[-1]

        print(path)

        if s == end:
            final_path = path
            break

        for n in graph[s]:
            if n not in path:
                copy_path = path[:]
                copy_path.append(n)
                queue.append(copy_path)
    
    return(final_path)

print(dfs(graph, 'YOU', 'SAN'))

final_path = dfs(graph, 'YOU', 'SAN')
print(f'Part 2: a minimum of {len(final_path)-3} orbital transfers are required between YOU and SAN')

