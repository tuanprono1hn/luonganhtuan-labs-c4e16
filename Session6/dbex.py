from pymongo import MongoClient
mongo_uri = "mongodb://admin1:admin1@ds117739.mlab.com:17739/c4e16-labs"
# 1. Connect to database
client = MongoClient(mongo_uri)
# 2. Get database
db = client.get_default_database()
# 3. Create collection
games = db["games"]
blog = db["blogs"]
# 4. Create document
new_game = {
    "name" : "Hứng bia",
    "description": "Bét game ever"
    }
# new_blog = [
#     {"Beauty":"Tâm sự dao kéo"},
#     {"Games":"Marvel vs DC Comic"},
#     {"Healthy life":"Cách chữa bệnh trĩ"},
#     {"Xe và đời sống":"Độ Wave thành Ex"}
#     ]
# # 5. Insert document into collection
# for i in range(len(new_blog)):
#     blog.insert_one(new_blog[i])
# games.insert_one(new_game)

all_game = games.find()

for game in all_game:
    print(game["name"])
