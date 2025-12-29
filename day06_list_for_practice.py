#python

ages = []
for i in range(5):
  age = int(input(f"Age : #No.{i+1}"))
  ages.append(age)
for age in ages:
  if age >= 18:
    print("adult")
  elif age >=12:
    print("teenager")
  else :
    print("child")
