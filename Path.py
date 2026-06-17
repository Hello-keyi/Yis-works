from pathlib import Path

path = Path('Forpath.py')
path1 = Path(r"C:\Users\yi\Desktop\Forpath1.txt")
a = path1.read_text()
print(path.read_text())
print(a)
lines = a.splitlines()
for i in lines:
    print(i)
b = ''
for i in lines:
    b += i
print(b)
path1.write_text("helo")