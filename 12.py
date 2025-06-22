from pprint import pprint

data = [
    {"front": "B", "to": "E"},
    {"front": "A", "to": "C"},
    {"front": "F", "to": "B"},
    {"front": "D", "to": "A"},
    {"front": "C", "to": "F"},
]

front, to = [], []
for i in data:
    front.append(i["front"])
    to.append(i["to"])

[start] = [i for i in front if i not in to] # тут деструктурировали взяв значение в скобки. у нас запишется просто строка а не список
# print(start)

newData = []
cursor = ""

while len(newData) != len(data):
    for el in data:
        if len(newData) == 0 and el.get("front") == start:
            newData.append(el)
            cursor = el["to"]
        else:
            if el.get("front") == cursor:
                newData.append(el)
                cursor = el["to"]
pprint(newData, indent=4)
