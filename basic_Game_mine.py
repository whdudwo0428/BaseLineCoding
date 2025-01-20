def print_minefield(N, grid):
    # 8방향 탐색을 위한 델타 값
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # 결과를 저장할 2차원 리스트
    result = [['0'] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:  # 지뢰가 있는 경우
                result[i][j] = '*'  # 지뢰를 '*'로 표현
            else:
                mine_count = 0
                # 주변 8방향의 좌표를 확인
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 1:
                        mine_count += 1
                result[i][j] = str(mine_count)  # 주변 지뢰 개수를 저장

    # 결과 출력
    for row in result:
        print(' '.join(row))


# Input 처리
N = int(input("NxN 크기를 입력하세요: "))

# NxN 크기의 리스트 입력 받기 (0은 빈칸, 1은 지뢰)
print(f"{N}x{N} 지뢰판 입력 (0은 빈칸, 1은 지뢰):")
grid = []
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# 지뢰 찾기 결과 출력
print_minefield(N, grid)
