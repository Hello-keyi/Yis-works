a = input("what is your first name?")
b = input("what is your last name?")
#这里是输入名字，接下来输出对话。
#我想要熟悉一下f和{}的用法。
c = f"{a} {b}".title()
print(f"Welcome {c}!")
print("Hello "+ b.title() + " " + a.title() + "!")
print(a + b)