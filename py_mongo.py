import pymongo
import pprint

from pymongo import MongoClient
client = MongoClient("localhost", 27017)

db = client.database_name
or
db = client['database_name']

collection = db.collection_name
or
collection = db["collection_name"]

# a sample document
post = {
    'author': 'Mike',
    'text': "My first blog post!",
    'tags': ['mongodb', 'python', 'pymongo'],
}

# inserting a document
posts = db.posts
post_id = posts.insert_one(post)

# get the first document
pprint.pprint(posts.find_one())

# insert one document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# querying for more than one document
for post in posts.find()
    pprint.pprint(post)
