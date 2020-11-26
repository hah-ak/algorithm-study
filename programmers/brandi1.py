
input_list = []
while True:
    try:
        input_list.append(int(input()))
    except EOFError:
        break

age = input_list[0]
simbak = input_list[1:]
max_sim = 220 - age
dic = {
    "90":0,
    "80":0,
    "75":0,
    "68":0,
    "60":0,
    "min":0
}
for i in simbak:
    if i >= max_sim * 0.9:
        dic["90"] += 1
    elif max_sim * 0.8 <= i:
        dic["80"] += 1
    elif max_sim * 0.75 <= i:
        dic["75"] += 1
    elif max_sim * 0.68 <= i:
        dic['68'] += 1
    elif max_sim * 0.6 <= i:
        dic['60'] += 1
    else:
        dic['min'] += 1
for v in dic.values():
    print(v, end= " ")

