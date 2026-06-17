"""
while True:
    print("Give me two numbers,and I will divide them.")
    print("If you want to quit the game,please enter 'q'.")
#我先给用户提示一下信息和操作和下面的代码几乎没什么关系
    
#-------------------------------------------------------------------------------------------------------------------

    first_number = input("What's your first number?")
#我弄出分子，接下来检验一下是不是退出的情况。

    if first_number == "q":
        break
#上面是检验退出的情况，接下来检验输入格式是否正确。

    try:
        a = int(first_number)
    except ValueError:
        print("To sure it is a number.")
        continue
#我这样检验了输入格式是否正确。 

#--------------------------------------------------------------------------------------------------

    second_number = input("What's your second number?")
#我弄出分母，接下来检验一下是不是退出的情况，再看看分母是不是0.

    if second_number == "q":
        break
    elif second_number == 0:
        print("YOU can't divide by 0.")
        
#上面是检验退出和分母是0的情况，接下来检验输入格式是否正确。
    try:
        b = int(second_number)
    except ValueError:
        print("To sure it is a number.") 
        
#我这样检验了输入格式是否正确，接下来计算就好了，两者做商.
    answer = a/b
    print(f"The answer is {answer}.")   

"""
#------------------------------------------------------------------------------------------

from pathlib import Path

def count_words (path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path("abc.txt")
count_words(path)

filenames = ["w.txt","e.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)

#-----------------------------------------------------------------------------------------
