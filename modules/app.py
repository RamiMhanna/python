import converters
from converters import kg_to_lbs

x = int(input("Enter the Weight in KG"))
print(f"{kg_to_lbs(x)}")
print(f"{converters.kg_to_lbs(x)}")