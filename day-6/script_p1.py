data = open("input.txt", "r")
data = data.read().split("\n")

matrix = []
si, sj, i, j = 0, 0, 0, 0

for line in data:
    matrix_line = []
    j = 0
    for symbol in line:
        if symbol == "#":
            matrix_line.append(1)
        elif symbol == ".":
            matrix_line.append(0)
        else:
            (si, sj) = (i, j)
        j += 1
    matrix.append(matrix_line)
    i += 1

i, j = si, sj
di, dj = -1, 0
count = 1
visited = []
while i + di < len(matrix) and i + di >= 0 and j + dj < len(matrix[0]) and j + dj >= 0:
    if matrix[i + di][j + dj] == 1:
        if (di, dj) == (-1, 0):
            (di, dj) = (0, 1)
        elif (di, dj) == (0, 1):
            (di, dj) = (1, 0)
        elif (di, dj) == (1, 0):
            (di, dj) = (0, -1)
        elif (di, dj) == (0, -1):
            (di, dj) = (-1, 0)
    if (i, j) not in visited:
        visited.append((i, j))
        count += 1
    i += di
    j += dj

print(count)
