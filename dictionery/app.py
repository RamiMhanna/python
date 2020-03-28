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
