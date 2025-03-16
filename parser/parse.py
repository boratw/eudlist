import json


with open("../original_src/Offset_Global.json", "rt", encoding='UTF-8-sig') as file:
    data = json.load(file)




#for i, a in enumerate(data):
    #del a["name_kr"]
    #del a["description_kr"]



with open("../src/Offset_Global.json", "wt", encoding='UTF-8-sig') as file:
    json.dump({"summary" : {}, "data" : data}, file, indent="    ", ensure_ascii=False)
