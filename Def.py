def great_user ():
    print("Hello")
great_user()



def great_username(user_name):
    print(f"Hello {user_name.title()}!")
great_username("li hua")



def players (name,job ="programer"):
    print(f"Hello {name},your job is {job}")
players("jack","doctor")



def position (x,y,z=4,a=3):
    print(x,y,z,a)
position(1,2,"",4)



def dic (first_name , last_name , age = None):
    person = {"first":first_name,
              "last":last_name,
              "age":age
              }
    return person
marry = dic("marry","poter",)
print(marry)
"""


def get_fullname(f_name,l_name):
    fullname = f"{f_name} {l_name}".title()
    return fullname
while True:
    print("Tell me what is your name,"
          "and I will back to you\n"
          "If you whant to quit it"
          ",please enter quit.")
    f_name = input("What's your first name?")
    f = f_name.title()
    if f == "Quit":
        print("Bye")
        break
    l_name = input("What's your last name?")
    l = l_name.title()
    if l == "Quit":
        print("Bye")
        break
    fullname = get_fullname(f_name,l_name)
    print(f"Hello {fullname}")

"""

def greet_users (names):
    for name in names:
        mg = f"Hello {name}"
        print(mg)
usernames = ["amili","bob","max","lily"]
greet_users(usernames)



def move (a,b):
    while a :
        c = a.pop()
        b.append(c)
    return b
ab = [1,2,3,4,5]
cd = [32,42,44,52]
print(move(ab[:],cd))
print(ab)
print(move(ab,cd))
print(ab)



def t (*abc):
    print(abc)
print(t(1,2,3,4,5,6))



def tt (a,b,*c):
    print(a)
    print(b)
    print(c)
print(tt(1,2,3,4,5,6,7,8,9,0))



dicc = {}
def built(a,*f) :
    dicc["first"]=a
    return dicc





