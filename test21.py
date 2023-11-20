animal_list = [
    ("ライオン", 58, "S"),
    ("チーター", 110, "C"),
    ("シマウマ", 60, "Z"),
    ("トナカイ", 80, "K"),
]
fasted_list = sorted(
    animal_list,
                        #listの三個目を元にして、並び替える
    key = lambda  ani : ani[2],
    reverse = True
    )

for i in fasted_list : print(i)