slst = ["名古屋","金山","神宮前"]
addlst = ["新安城","東岡崎","豊橋"]

# 要素を追加
slst.append("知立")

# 二つのリストを結合
lst = slst + addlst

# 要素の削除
del lst[4]

# 93ページをチェック
for i, val in enumerate(lst):
    print(i, val)

print(list(enumerate(lst)))