from pathlib import Path
import json

path = Path("username.py")
if path.exists():
    contens = path.read_text()
    usnername = json.loads(contens)
    print(f"Whelcome back {usnername}.")
else:
    usnername = input(f"What's your name?")
    contens = json.dumps(usnername)
    path.write_text(contens)
    print(f"We'll remember you when you back,{usnername}.")