animal_list = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}
fasted_list = sorted(animal_list)
for name in animal_list.keys() :
    value = animal_list[name]
    print( name, value )