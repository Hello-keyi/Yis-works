dic = {
    "num":"3",
    "word":"man"
    }

print(dic["num"])

dic [
    "color"
    ] = "blue"
del dic ["num"]

print(dic)
print(dic.get("color","none here"))
print(dic.get("num","no num here"))


for key,value in dic.items() :
    print(f"here is {key}")
    print(f"here is {value}")


for key in sorted(dic.keys()):
    print(f"the key is {key} ")


for value in dic.values():
    print(f"the value is {value}")


dic ["list"] = [1,2,3,4,5]
print(dic)
for i in dic["list"]:
    print(i)
    

User ={"Bob":{
    "name":"bob",
    "age":"5"
    },

    "Mary":{
    "name":"bob",
    "age":"5"
    }
}