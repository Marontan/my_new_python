# json
import json
with open("my_json.json", "r") as f:
    cont = f.read()
    j = json.loads(cont)
    print(j["widget"].keys())

# csv
import csv

myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]
myFile = open('output.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)


# pickle
import pickle

class Foo:
    bar = "bar"

a = [1, 10, 0, -3, 9]
foo = Foo()
with open("pickle", "wb") as f:
    pickle.dump(foo, f)

with open("pickle", "rb") as f:
    aa = pickle.load(f)
    print(aa.bar)