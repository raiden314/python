while True:
    h = input("身長をcmで入力してください")
    w = input("体重をkgで入力してください")
    try :
        h = float(h) / 100
        w = float(w)
        bmi = w / ( h * h )
        break
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except :
        print( "エラー：もう一度入力してください" )
str = "あなたのBMI値は" + str(bmi) + "です"
print( str )