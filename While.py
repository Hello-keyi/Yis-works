a = "234"
print(a)
print(int(a)+2)
print(122%3)

print("write a word and i will repeat it back to you\n" \
    "if you want to quit the program ,please input quit")


a = ""
'''
while a != "quit":
    a = input()
    print(a)
    if a == "quit":
        print("end")
        break
'''
#测试用户输入

i = 1
num = [i for i in range (1,11)]
while i in num :
    
    i += 1
    if i == 7:
        continue
    print(i)

num .append(7)
print(num)
num1 = []

while 7 in num :
    num.remove(7)
    print(num)
    num1 .append(7)


print(num)
print(num1)

a = True
dic = {}
while a :
    what = input("what").lower()
    when = input("when").lower()
    dic [when] = when
    dic [what] = what
    if what == "no":
        a = False
print(dic)









