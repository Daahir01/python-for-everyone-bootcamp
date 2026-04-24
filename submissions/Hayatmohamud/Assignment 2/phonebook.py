# Declaration of the phone book dictionary
phone_book = {
    "Ali": "0612345678",
    "Ayaan": "0623456789",
    "Hassan": "0634567890"
}


print("Ali's number:", phone_book.get("Ali"))  # exists
print("Fatima's number:", phone_book.get("Fatima", "unknown"))  # does NOT exist

print("\n-- Using keys --")
for name in phone_book:
    print(name, "->", phone_book[name])


print("\n-- Using items() --")
for name, number in phone_book.items():
    print(name, ":", number)