#python
#Store age + Classifiaction
#------------wrong---------------

#records = []

#for i in range(5):
#  age = int(input(f"Age No.{i+1}: "))
#  if age >= 18:
#     group = "Adult"
#  elif age >=14:
#     group = "Teenager"
#  else:
#     group = "Children"

#records = {"Age" : age , "Group" : group}
#records.append(record)

#print(f"\n---Summary---")
#for record in records:
#  print(f"age = record['age'] -->  group = record['age']")

#---------------currect answer-------------------
records = []

for i in range(5):
  age = int(input(f"Age No.{i+1}: "))
  if age >= 18:
     group = "Adult"
  elif age >=14:
     group = "Teenager"
  else:
     group = "Children"
  record = {"Age" : age , "Group" : group}
  records.append(record)


print(f"\n---Summary---")
for record in records:
  print(f"age = {record['Age']} -->  group = {record['Group']}")
