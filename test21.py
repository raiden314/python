animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ", 80),
]
fasted_list = sorted(
    animal_list,
                        #listの一番始めを取る
    key = lambda  ani : ani[1],
    reverse = True
    )

for i in fasted_list : print(i)