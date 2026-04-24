

while True:
    text = input("Type something (or 'done' to quit): ")

    if text == "done":  # only lowercase "done" is accepted
        break

    print("You typed:", text)

print("Goodbye!")