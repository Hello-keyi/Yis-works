def hello ():
    print("Hello")



def get_fullname(f_name,l_name):
    fullname = f"{f_name} {l_name}".title()
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
    return fullname


