import json
from pymongo import MongoClient

with open("config.json", "r+") as f:
    data = json.load(f)

    DATABASE_URL = data["DATABASE_URL"]
    DATABASE_NAME = data["DATABASE_NAME"]






cluster = MongoClient("mongodb://127.0.0.1:27017")
chat_db = cluster.get_database("dpapi")
users_collection = chat_db.get_collection("users")
message_collection = chat_db.get_collection("message")




user = "None"
msg = "None"
while True:
    message = message_collection.find({})
    for x in message:
        if msg != x["message"] and user != x["user"]:
            print(f"User - ", x["user"], "Message - ", x["message"])

            msg = x["message"]





