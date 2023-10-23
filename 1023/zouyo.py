amt = input("年間の贈与額は何万円ですか？")
tax = 0
amt = int(amt) - 110
if amt <= 0 : 
    pass
elif amt <= 200 :
    tax = amt * 0.1  -   0
elif amt <= 300 :
    tax = amt * 0.15 -  10
elif amt <= 400 :
    tax = amt * 0.2  -  25
elif amt <= 600 :
    tax = amt * 0.3  -  65
elif amt <= 1000 :
    tax = amt * 0.4  - 125
elif amt <= 1500 :
    tax = amt * 0.45 - 175
elif amt <= 3000 :
    tax = amt * 0.5  - 250
else :
    tax = amt * 0.55 - 400
print("贈与税額は"+str(tax)+"万円です")