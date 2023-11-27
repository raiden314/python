import calcFunc

#1
amount = input("売買価格を入力してください")
fee = calcFunc.feeCalc(float(amount))
print("仲介手数料は" +  str(fee) + "万円です")