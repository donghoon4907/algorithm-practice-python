N, L = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(N)]

def check(arr):
    visited = [False for _ in range(N)]

    for i in range(N - 1):
        # 현재 칸과 다음 칸의 높이가 같은 경우
        if arr[i] == arr[i + 1]:
            continue
        # 현재 칸과 다음 칸의 높이 차이가 1이상인 경우
        elif abs(arr[i] - arr[i + 1]) > 1:
            return False
        # 현재 칸의 높이가 다음 칸의 높이 보다 높은 경우(내리막 경사로)
        elif arr[i] > arr[i + 1]:
            height = arr[i + 1]
            # 경사로의 범위크기 만큼 순회
            for j in range(i + 1, i + L + 1):
                # 경사로의 길이가 길의 범위 내에 포함되는 경우
                if 0 <= j < N:
                    # 경사로를 놓을 칸의 높이가 다른 경우 or 이미 경사로가 놓인 경우
                    if height != arr[j] or visited[j]:
                        return False
                    # 경사로 처리
                    visited[j] = True
                else:
                    return False
        # 다음 칸의 높이가 현재 칸의 높이 보다 높은 경우(오르막 경사로)
        else: 
            height = arr[i]
            # 경사로의 범위크기 만큼 순회
            for j in range(i, i - L, -1):
                # 경사로의 길이가 길의 범위 내에 포함되는 경우
                if 0 <= j < N:
                    # 경사로를 놓을 칸의 높이가 다른 경우 or 이미 경사로가 놓은 경우
                    if height != arr[j] or visited[j]:
                        return False
                    # 경사로 처리
                    visited[j] = True
                else: 
                    return False
    return True
    
answer = 0
# 가로 길 체크
for load in matrix:
    if check(load):
        answer += 1
# 세로 길 체크
for i in range(N):
    load = [matrix[j][i] for j in range(N)]
    if check(load):
        answer += 1

print(answer)