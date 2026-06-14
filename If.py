num = [i for i in range (1,6)]
print(num)
i = 3
if i in num:
    print(f"{i} in the list")
else:
    print(f"{i}dont in the list")
num.clear()
if num:
    print("there is something in the list")
else:
    print('none')