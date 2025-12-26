#python
用 for 跑 3 次
每次輸入一個年齡
用 if 判斷成人 / 未成年
每次都印結果

for i in range(3):
  age= int(input("Age: "))
  if age >= 18:
    print("adult")
  else :
    print("minor")
