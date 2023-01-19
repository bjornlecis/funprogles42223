persoon = {"naam":"Bjorn","leefijd":31,"hobbies":["Lopen","Zwemmnen","Python"]}
for key in persoon.keys():
    print(key,end="\t")
print("")
for value in persoon.values():
    if isinstance(value,list):
        for item in value:
            print(item,end=" ")
    else:
        print(value,end="\t")
print("")
print("-------")
persoon["woonplaats"] = "Bilzen"
for key in persoon.keys():
    print(key,end="\t")
print("")
for value in persoon.values():
    if isinstance(value,list):
        for item in value:
            print(item,end=" ")
    else:
        print(value,end="\t")



