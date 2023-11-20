while True:
    try :
        h = input("身長をcmで入力してください")
        w = input("体重をkgで入力してください")
        h = float(h) / 100
        w = float(w)
        bmi = w / ( h * h )
        break
    except :
        print( "エラー：もう一度入力してください" )
str = "あなたのBMI値は" + str(bmi) + "です"
print( str )