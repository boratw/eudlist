import json


with open("1.json", "rt", encoding='UTF-8-sig') as file:
    arr = json.load(file)

arr.sort(key=lambda x : x["name"][:4])
for x in arr:
    x["union"] = x["name"][ : (x["name"].find("-") - 1)]

with open("2.json", "wt", encoding='UTF-8-sig') as file:
    json.dump(arr, file, indent="    ", ensure_ascii=False)
