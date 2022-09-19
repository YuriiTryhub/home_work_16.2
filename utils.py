import json

def init_db():
    with open('data/user.json') as file:
        a = json.load(file)
        print(a)

print(init_db())