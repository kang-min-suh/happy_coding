from collections import deque
def bfs_city(start): 
    q = deque()
    INF = float("inf")
    distance = [INF]*(n+1)
    q.append(start)
    distance[start] = 0

    while q: 
        for next_node in graph[now]:
            if distance[nex_node] == INF: 
                distance[nex_node] = distance[now] + 1
                q.append(next_node)
        return distance 
    
    