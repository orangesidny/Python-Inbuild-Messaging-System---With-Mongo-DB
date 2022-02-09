import json
from pymongo import MongoClient

with open("config.json", "r+") as f:
    data = json.load(f)

    DATABASE_URL = data["DATABASE_URL"]
    DATABASE_NAME = data["DATABASE_NAME"]





cluster = MongoClient(DATABASE_URL)
chat_db = cluster.get_database(DATABASE_NAME)
users_collection = chat_db.get_collection("users")
message_collection = chat_db.get_collection("message")

def save_user(username, password):
    users_collection.insert_one({
        "_id": username,
        "password": password
    })

def set_message():
    message_collection.insert_one({
        "_id": "message",
        "user": "USERR",
        "message": "None"
    })




def add_message(usern):
    msg = input("Please input the message you want to send - ")

    myquery = {"_id": "message"}
    newvalues = {"$set": {"_id": "message", "user": usern, "message":msg}}

    x = message_collection.update_one(myquery, newvalues)



results = users_collection.find({})
message = message_collection.find({})


def login():
    print("""
WELCOME TO THE INBUIT PYTHON MESSAGING SYSTEM Made by orangesidny#7777
DISCORD - orangesidny#7777
GITHUB - https://github.com/orangesidny
DISCORD SERVER - https://discord.gg/4qCugg5nmw
DISCORD BOT STORE - http://oranges.host/store
ITS OPEN SOURCE SO ITS FREE 
    """)
    selc = input("Type `login` to login or `signup` to signup- \n")
    if selc == "login":
        usern = input("Enter your username - \n")
        passn = input("Enter your password - \n")

        x = users_collection.find_one({"_id": usern,"password": passn})
        if x is None:
            print("No Login Found \n\n")
            login()
        else:
            print("Successfully logged in")
            try:
                message_collection.insert_one({
                    "_id": "message",
                    "user": usern,
                    "message": "None"
                })
            except:
                pass
            print("Please make sure you have the messagingconsole OPEN")

            while True:
                add_message(usern)



    elif selc == "signup":
        usern = input("Enter username - \n")
        passn = input("Enter password - \n")
        try:
            save_user(f"{usern}", f"{passn}")
        except:
            print("Username already exists")
    else:
        print("Sorry to tell you but you cant spell")
        login()

try:
    set_message()
except:
    pass

login()

