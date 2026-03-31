# Example: User input creates keys

people = {}

count = int(input("How many people? "))

for i in range(count):
    name = input(f"Name #{i+1}: ")
    age = int(input("Age: "))

    people[name] = age   # ← key 來自使用者，不是寫死

print("\n--- Search ---")
search_name = input("Who do you want to check? ")

if search_name in people:
    print(f"{search_name} is {people[search_name]} years old.")
else:
    print("Not found.")
