from collections import deque

N, M, K = list(map(int, input().split()))

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))
# K번 남았을 때 이동한거리
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    # 출발지 설정(x좌표, y좌표, 벽을 깰 수 있는 남은 횟수)
    q = deque([(a, b, K)])
    # 출발지 이동한 횟수 + 1(시작하는 칸포함)
    visited[a][b][K] = 1

    while q:
        x, y, k = q.popleft()
        # 목적지에 도착한 경우
        if x == N - 1 and y == M - 1:
            return visited[x][y][k]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 다음 목적지가 벽인 경우(and방문하지 않은 경우)
                if k > 0 and matrix[nx][ny] == 1 and visited[nx][ny][k - 1] == 0:
                    # 이동한 횟수 + 1
                    visited[nx][ny][k - 1] = visited[x][y][k] + 1
                    q.append((nx, ny, k - 1))
                # 다음 목적지가 벽이 아닌 경우(and방문하지 않은 경우)
                elif matrix[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    # 이동한 횟수 + 1
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    q.append((nx, ny, k))
    return -1

print(bfs(0, 0))