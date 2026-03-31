#python

name=input("Name: ")

for i in range(5,10):
   age=int(input("Age: "))
   if age>=18:
     print(f"{name} is an adult.")
   elif age>=14:
     print(f"{name} is a teenager.")
   else: 
     print(f"{name} is a child.")
