data = open("input.txt", "r")
data  = data.read().split("\n")

def get_transpose(matrix):
    tr = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    res = []
    for line in tr:
        res.append("".join(line))
    return res

def get_diagonals(matrix, back=False):
    diagonals = []
    n = len(matrix)
    for offset in range(1-n, n):
        if not back:
            diagonal = [matrix[i][i + offset] for i in range(n) if 0 <= i + offset < n]
        else:
            diagonal = [matrix[i][n-1-i+offset] for i in range(n) if 0 <= n-1-i+offset < n]
        diagonals.append(diagonal)
    res = []
    for line in diagonals:
        res.append("".join(line))
    return res

def find_xmas(matrix):
    sum = 0
    for line in matrix:
        sum += len(line.split("XMAS")) - 1
        sum += len(line.split("SAMX")) - 1
    return  sum

sum = 0
sum += find_xmas(data)

data = get_transpose(data)
sum += find_xmas(data)

data_diag = get_diagonals(data)
sum += find_xmas(data_diag)

data_diag = get_diagonals(data, True)
sum += find_xmas(data_diag)

print(sum)