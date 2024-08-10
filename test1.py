N, L = list(map(int, input().split()))

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
visited = [[False] * N for _ in range(N)]

result = 0
for i in range(N):
    # 경사로 설치 여부
    flag = True
    for j in range(N - 1):
        # 높이가 다른 경우
        if matrix[i][j] != matrix[i][j + 1]:
            # 경사로를 놓을 수 있는지 검증
            count = 0
            for k in range(L):
                count += matrix[i][j] - matrix[i][j + k]
                # 방문 처리
                visited[i][j + k] = True
            # 경사로를 설치한 높이 차이 검증
            if abs(count) != L:
                flag = False
                break
    # 경사로 설치에 문제가 없는 경우
    if flag:
       result += 1 

print(result)