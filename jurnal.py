
vcount = 0
vMan = 0
vWoman = 0
vAdult = 0
lNames = []
lAgesSorted = []
lManOver35 = []
lManOver35F = []
lCommonNamesTMP = []
lCommonNames = []
dCommonNames = {}
persons = [
    {
        "name": "Anna",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Keanu",
        "age": 57,
        "gender": "male"
    }, {
        "name": "Angelina",
        "age": 46,
        "gender": "female"
    }, {
        "name": "Alex",
        "age": 42,
        "gender": "male"
    }, {
        "name": "Cortana",
        "age": 25,
        "gender": "female"
    }, {
        "name": "Carlsen",
        "age": 31,
        "gender": "male"
    }, {
        "name": "Jan",
        "age": 31,
        "gender": "male"
    },{
        "name": "Florentino",
        "age": 74,
        "gender": "male"
    },{
        "name": "Angelina",
        "age": 16,
        "gender": "female"
    },{
        "name": "Alex",
        "age": 22,
        "gender": "male"
    },{
        "name": "Alex",
        "age": 15,
        "gender": "male"
    },{
        "name": "Alex",
        "age": 55,
        "gender": "female"
    },{
        "name": "Jan",
        "age": 30,
        "gender": "male"
    }
]

for i in persons:
    vcount = vcount + 1
    if i["gender"] == 'male':
        vMan = vMan + 1
    else:
        vWoman = vWoman + 1
    if i["age"] > 18:
        vAdult = vAdult + 1
    if i["gender"] == 'male' and i["age"] > 35: #отобрали в список мужчин старше 35 (позже отфильтруем список по первой букве F в имени)
        lManOver35.append(i["name"])
    if i["age"] not in lAgesSorted:
       lAgesSorted.append(i["age"])
    lNames.append(i["name"])
    if i["name"] not in dCommonNames:           #создется словарь с именем в значении и количеством раз, которое это имя встречается в словаре словарей, в ключе
        dCommonNames[i["name"]] = 1
    else:
        dCommonNames[i["name"]] += 1
for j in lManOver35:                            #фильтруем список по первой букве F в имени
    if j[0] == 'F':
        lManOver35F.append(j)
lAgesSorted.sort()
lCommonNamesTMP = list(dCommonNames.items())
lCommonNamesTMP.sort(key=lambda i: i[1], reverse = True)
print(f'lCommonNamesTMP {lCommonNamesTMP}')
k = 0
for i, j in lCommonNamesTMP:
    if k < 3:
        lCommonNames.append(i)
    k += 1

print(f"В словаре Всего: {vcount}. Из них:\n \tмужчин: {vMan} \n \tженщин: {vWoman} \n \tсовершеннолетних: {vAdult}")
print(f"В словаре присутствуют: {lNames}")
print(f"Из них мужчины старше 35, имена которых начинаются с F: {lManOver35F}")
print(f"В словаре присутствуют люди следующих возростов: {lAgesSorted}")
print(f"Три самых распространенных имени в словаре: {lCommonNames}")