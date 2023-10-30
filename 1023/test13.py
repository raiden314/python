# 1-6

# 49+6=55
# 55-4=51
# 51-2=49
# 49+1=50
import random
sum = 0
cnt = 0
# while sum != 50 :
#     if sum >= 0 | sum <50 :
#         i = random.randint(1,6)
#         sum = sum + i
#         cnt = cnt + 1
#     elif sum > 50 :
#         i = random.randint(1,6)
#         sum = sum - i
#         cnt = cnt + 1
#     print(cnt,"回目","今回の目は",i,"合計は",sum)
# print("結果、さいころを振った回数は",cnt)

for i in range(20) :
    num = random.randint(1,6) #1-6
    cnt = cnt + 1
    if( sum < 50 ) :
        sum = sum + num
    elif( sum > 50) :
        sum = sum - sum
    print(cnt,"回目＝",num)
    print("合計＝",sum)
    if ( sum == 50 ):
        break
else :
    print("強制終了")
