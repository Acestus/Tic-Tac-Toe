numbers = [int(n) for n in input()]
print([sum(numbers[0:x]) for x in range(1, len(numbers) + 1)])