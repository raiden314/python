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
        print("エラー：整数を入力してください")
    except ZeroDivisionError as e:
        print(e)
        print("エラー：身長に0を入力しないでください")
    except :
        print( "エラー：もう一度入力してください" )
    finally :
        print("BMI計算")
str = "あなたのBMI値は" + str(bmi) + "です"
print( str )