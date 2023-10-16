# age = input("生まれた年は（西暦）は？")
# print( age )
year = input("生まれた年は（西暦）は？")
# 演算するために変数yearを整数型に型変換
age = 2023 - int( year )
# 文字列結合するために変数ageを文字列型に型変換
print( "2023年あなたは" + str( age ) + "歳です" )