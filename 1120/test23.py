#ファイル名を関数名と同じにすると動かなくなる
def genIto3():
    yield 1
    yield 2
    yield 3
it = genIto3()
for  i in it:
    print(i)