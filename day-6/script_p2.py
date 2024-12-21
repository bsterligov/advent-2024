data = open("input.txt", "r")

matrix = {
    i + j * 1j: c
    for i, r in enumerate(data)
    for j, c in enumerate(r.strip())
}

start = min(p for p in matrix if matrix[p] == "^")


def walk(data):
    pos, dir, visited = start, -1, set()
    while pos in data and (pos, dir) not in visited:
        visited |= {(pos, dir)}
        if data.get(pos + dir) == "#":
            dir *= -1j
        else:
            pos += dir
    return {p for p, _ in visited}, (pos, dir) in visited


path = walk(matrix)[0]
print(sum(walk(matrix | {x: "#"})[1] for x in path))
