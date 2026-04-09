li = [
    [1, 2, 3, 4],
    [5, 6, 7, 3],
    [4, 5, 8, 6],
    [1, 4, 3, 2]
]

# 방향배열
# 0: 상, 1:하, 2: 좌, 3: 우
dy = [-1, 1, 0, 0]
dx = [0,0,-1, 1]

y, x = map(int, input().split())
total = 0
for i in range(4):
    ny = y + dy[i] # 현재 y좌표에서 i번째 방향의 offset을 더해주면
    # i번째 방향의 위치로 간다.
    # (ny, nx) = i:0
    nx = x + dx[i]
    # 바운더리 체크
    # 뭐뭐 하세요 보다 뭐뭐 하지 마세요 조건으로 설계
    if ny >= 0 and nx >= 0 and ny < 4 and nx< 4 and li[ny][nx] % 2 ==1:
        if ny < 0 or nx < 0 or ny>= 4 or nx >= 4:
            continue

        total += li[ny][nx]
print(total)