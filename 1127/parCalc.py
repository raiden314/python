import calcFunc
amount = input("売買価格を入力してください")
amount = float(amount)
fee = calcFunc.feeCalc(amount)
print("仲介手数料は" +  str(fee) + "万円です")