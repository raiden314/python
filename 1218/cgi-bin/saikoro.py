import sys,io,random
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, 
    encoding='utf-8'
)#文字化けしないために必要

#ヘッダーを出力
print("Content-Type: text/html; charset=utf-8")
print("")

# ランダムな数を取得
no = random.randint(1, 6)
# 画面に出力
print("""
<html>
<head><title>Dice</title></head>
<body>
    <h1>{num}</h1>
</body>
</html>
""".format(num=no))