var0 = 33.0
var1 = 'Hello'
var2 = """sfsd sdf 
sdf sdf
sdf"""
var3 = True
var4 = bool(var1)

print(var0)
print(var1)
print(var2)
print(var4, "test")
# print("Hello World")

lst = [1, "e", "43", True, [1,2,3]]

range(2,4,1)
t2 = (5,6,7)
t3 = t2[:]
print(t3)

dics = {
    "first": 2,
    "second": True
}
dics["first"] = 1
dics[True] = 33

print(dics.values())
print(22,'\n', "werwer")

t4 = [0,1,2,3,4]
t5 = [i**3 for i in t4]
print(t4)
print(t5)

t6 = ["asrrd","sdsdsdsd","sds"]
t7 = [len(i) for i in t6]
print(t7)

s1 = "123"
s2 = "456"
print(f"as {int(s1)*2} sfsdf {s2} dsfdfs {t6}")


foo = lambda x, y: [x**2, y**3]
print(foo(44, 2))

print([(lambda x: x[0])(word) for word in t6])

def is_allowed_to_smoke(age: int) -> bool:
    if age < 18 or age > 65:
        return False
    elif age == 18:
        return True
    return True
    # return age >= 18
print(is_allowed_to_smoke(184))


i = 0
while i<100:
    i+=1
print (i)

q1= [0,1,2,3]
for i in q1:
    q1[i] += 5

for i in range(2, 11, 2):
    i+=1