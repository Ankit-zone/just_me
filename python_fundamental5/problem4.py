import json

py_obj = {"Maharashtra": 50000}
try:
    with open("cities.json","r") as f:
        data=json.load(f)
except FileNotFoundError:
    data={}
data.update(py_obj)

with open("cities.json","w") as f:
    json.dump(data,f,indent=4)