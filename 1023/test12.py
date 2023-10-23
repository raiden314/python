import random
s = ["大吉","中吉","小吉","凶"]
# randomってどこから持ってきているかわからないため、randomに波線が引かれる
i = random.randint(1,3)
print( s[i] )