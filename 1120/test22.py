animal_list = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}
#タプルの形で返ってくる
faster_list = sorted(
        #引数の最初は、データ型なんでも引き入れてくれる
        animal_list.items(),
        key = lambda x : x[1],
    ) #引数と戻り値は一緒
for name, value in faster_list :
    print( name,value )