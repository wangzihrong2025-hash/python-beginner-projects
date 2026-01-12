#python

#Day8: Count groups (standalone)

recoder=[
      {"Group":"Adult"},
      {"Group":"Teenager"},
      {"Group":"Children"},  
]

adult =0
tennanger = 0
children = 0

for recoder in recoders:
  if recoder["Group"] == "Adult":
     adult += 1
elif recoder["Group"] == "Teenager":
     teenager += 1
else recoder["Group"] == "Child":
     children +=1

print("---Count---")
print("Adult",adult)
print("Teenager",teenager)
print("Children",children)


