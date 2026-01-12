#python

#Day8: Count groups (standalone)

recoders=[
      {"Group":"Adult"},
      {"Group":"Teenager"},
      {"Group":"Children"},  
]

adult =0
teenager = 0
children = 0

for recoder in recoders:
    if recoder["Group"] == "Adult":
        adult += 1
    elif recoder["Group"] == "Teenager":
        teenager += 1
    else :
         children +=1

print("---Count---")
print("Adult",adult)
print("Teenager",teenager)
print("Children",children)


