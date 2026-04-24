nums = list(range(10))
print("Every second value:", nums[::2])
print("Reversed list:", nums[::-1])

# Use a for loop with range(3, 8)
print("\nNumbers from 3 to 7:")
for i in range(3, 8):
    print(i)

# Use enumerate on a list of words
words = ["go", "python", "code"]
print("\nEnumerate words:")
for index, word in enumerate(words):
    print(f"{index}: {word}")

# Build a small dictionary and loop with items()
d = {
    "a": 1,
    "b": 2
}
print("\nDictionary items:")
for k, v in d.items():
    print(f"{k} -> {v}")