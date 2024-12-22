data = open("input.txt", "r")


def equals(sum, numbers):
    def backtrack(index, current_value):
        if index == len(numbers):
            return current_value == sum

        if backtrack(index + 1, current_value + numbers[index]):
            return True

        if backtrack(index + 1, current_value * numbers[index]):
            return True

        if backtrack(index + 1, int(f"{current_value}{numbers[index]}")):
            return True

        return False

    return backtrack(1, numbers[0])


result = 0
for line in data:
    eval, numbers = line.strip().split(": ")

    eval = int(eval)
    numbers = list(map(int, numbers.split()))

    result += eval if equals(eval, numbers) else 0

print(result)
