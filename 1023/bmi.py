h = input("身長をcmで入力してください")
w = input("体重をkgで入力してください")
h = float(h) / 100
w = float(w)
bmi = w / ( h * h )
result = ""
if bmi < 18.5 :
    result = "痩せ型"
elif bmi < 25 :
    result = "標準体重"
elif bmi < 30 :
    result = "肥満(軽)"
else :
    result = "肥満(重)"
str = "あなたのBMI値は" + str(bmi) + "です"
print( str )
print( "判定：" + result )