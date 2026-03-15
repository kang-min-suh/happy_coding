graph = {
    'E': set(['D', 'A']),
    'D': set(['E', 'F']),
    'A': set(['E', 'C', 'B']),
    'F': set(['D']),
    'C': set(['A']),
    'B': set(['A'])
}

# 입력 예시: E B (E에서 시작해서 B까지 가는 최단 거리)
start, end = input("시작 노드와 목표 노드를 입력하세요(예: E B): ").split()

queue = [start]     # 앞으로 방문할 곳 (줄 서는 곳)
visited = [start]   # 이미 방문한 곳 (다시 안 가려고 기록)

def solution():
    count = -1 # '층' 혹은 '거리'를 나타냄  # 나자신과의 거리는 0을 만들기 위한 세팅 

    while len(queue) != 0:
        count += 1
        size = len(queue) # 현재 층에 몇 명이 줄 서 있는지 확인
        
        for i in range(size):
            node = queue.pop(0) # 줄의 맨 앞사람을 꺼냄
            
            if node == end:
                return count # 목표를 찾으면 현재 몇 층인지 반환

            # 연결된 다음 노드들을 확인
            for next_node in graph[node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.append(next_node)
    return count

print(f"결과(최단 거리): {solution()}")