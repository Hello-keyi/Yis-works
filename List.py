num = [1,2,3,4,5]
print(num)
print(num[2])
pep = ['a','b','c','d','e','f','g','h','i','j']
print(pep[4])
print(pep[3].upper())
print(num[3]+num[3])
print(f"{num[3]} = 4")
num [2] = 2
print(num)
num [2] = 3
num.append(6)
print(num)
del num [0]
print(num)
num.append(7)
print(num)
x = num.pop(2)
print(num)
print(x)
y = 7
num.remove(y)
print(num)
print(y)


word = ['morinig','happy','sun','river','hello','good','light','swing']
print(word)
word.sort()
print(word)
word.sort(reverse = True)
print(word)

print(f"这是原来的{word}\n")
print(f"这是改后的{sorted(word)}")
print(f"\n现在是{word}")
word.reverse()
print(word)
word.reverse()
print(word)

print(len(num))
print(len(pep))
print(len(word))
print(word[-2])
for w in word:
    print(f'{w}in the list\n')

for i in range(1,100):
    print(i)

