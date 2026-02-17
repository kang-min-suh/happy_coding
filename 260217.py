s = input()

chunks = s.split(",")

cleaned = [chunk.strip() for chunk in chunks]
print(cleaned)
numbers = [int(x) for x in cleaned]
print(numbers)