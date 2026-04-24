# Original string with extra spaces and commas
line = "  Hello, you, WORL D "

# Clean the string: strip spaces and convert to lowercase
cleaned = line.strip().lower()
print("Cleaned:", cleaned)

# Split the string by comma
parts = cleaned.split(",")
print("Split parts:", parts)

# Build a list using append
words = []
words.append("python")
words.append("is")
words.append("fun")

print("Appended list:", words)