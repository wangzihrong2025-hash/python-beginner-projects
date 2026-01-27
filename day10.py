#python

records = []

count = int(input("How many people? "))
for i in range(count):
    age = int(input(f"Age #{i+1}: "))

    if age >= 18 :
        group = "Adult"
    elif age >=13 :
        group = "Teenager"
    else :
        group = "Child"

    record = {
      "age" : age,
      "group" : group
    }
    records.append(record)

adult = 0
teenager = 0
child = 0

for a in records :
    if a["group"] == "Adult":
        adult +=1
    elif a["group"] == "Teenager":
        teenager +=1
    else a["group"] == "Child"
        child +=1

print(" \n----Result")
print("Adult:" , adult )
print("Teenager:" , teenager)  
print("Child:" , child)
