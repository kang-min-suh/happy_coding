from typing import Counter
graph = {'A': set(['B', 'C']), 
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']), 
         'D': set(['B']), 
         'E': set(['B', 'F']), 
         'F': set(['C', 'E'])
         }

start, end = [i for i in input().split(' ') ]
queue = [start]
visited = [start]

def solution():
    count = -1 

    while len(queue) != 0: 
        count += 1
        size = len(queue)
        print(f'count는 {count}')
        for i in range(size):
            node = queue.pop(0)
            print(f'    node는 {node}')
            if node == end: 
                return count

            for next_node in graph[node]
                print(f'      graph[node]는 {graph[node]}')
                print(f'      next_node는 {next_node}')
                if next_node not in visited: 
                    queue.append(next_node)
                    visited.append(next_node)

    return count

print(solution())
