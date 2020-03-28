persons = {
    "name": "Rami",
    "age": 30,
    "phone": "5456468765",
    "Email": "rami.mhanna@powercoders.org",
    "is_verified": True
}
print(persons["age"])
print(persons.get("age"))
print(persons.get("Age"))
print(persons.get("Age", "50"))

persons["member"] = False
print(persons)


print("_" * 130)

digits = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE"
}
output = ""
INPUT = input("Phone:")
for digit in INPUT:
    output += digits[digit]
    output += "  "

print(f"The written number is: {output}")
