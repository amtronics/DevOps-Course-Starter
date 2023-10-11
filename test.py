import pymongo
client = pymongo.MongoClient("mongodb://mod10:8mRoMlkZm9pqVA8t4Q19cD7aZi0VXM2UYWKke7xuwewqVhxl6DDgIkduhONvHnjsiKXah9vlwfEHACDbbqhN2Q==@mod10.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@mod10@")
db = client.todoapp
collection = db.todo_items
client.list_database_names()


# import datetime
# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
# }
# post_id = collection.insert_one(post).inserted_id