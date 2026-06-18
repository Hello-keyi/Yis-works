from pathlib import Path
import json




numbers = [1,2,3,4,5,6,7,8,9]

path = Path("numbers.json")
contens = json.dumps(numbers)
contens = path.read_text()
numbers = json.loads(contens)
print(numbers)

#-------------------------------------------------------------------------------


username = input("What's your name?")

path = Path("username.json")
contens = json.dumps(username)
path.write_text(contens)

print(f"I'll remember it,{username}.")


#------------------------------------------------------------------------------------




contens = path.read_text()
username = json.loads(contens)
print(f"Hello {username}!")


