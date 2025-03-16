import json


namearr = []
descarr = []
with open("../src/Offset_CUnit.json", "rt", encoding='UTF-8-sig') as file:
    arr = json.load(file)


with open("../src/tr_name.txt", "rt", encoding='UTF-8-sig') as file:
    for s in file.readlines():
        namearr.append(s[:-1])

with open("../src/tr_desc.txt", "rt", encoding='UTF-8-sig') as file:
    for s in file.readlines():
        descarr.append(s[:-1])

for i, a in enumerate(arr):
    a["name_kr"] = namearr[i]
    a["description_kr"] = descarr[i]



with open("../src/Offset_CUnit_new.json", "wt", encoding='UTF-8-sig') as file:
    json.dump(arr, file, indent="    ", ensure_ascii=False)
