import json


with open("../src/Offset_Global.json", "rt", encoding='UTF-8-sig') as file:
    arr = json.load(file)

namearr = []
descarr = []
offsetarr = []
for a in arr["data"]:
    namearr.append(a["name"]["en"])
    descarr.append(a["description"]["en"])
    offsetarr.append(a["offset"])



with open("../src/tr_name.txt", "wt") as file:
    for s in namearr:
        file.write(s + "\n")

with open("../src/tr_desc.txt", "wt") as file:
    for s in descarr:
        file.write(s + "\n")

with open("../src/tr_offset.txt", "wt") as file:
    for s in offsetarr:
        file.write(s + "\n")