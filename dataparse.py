import pymongo, random, json

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection["AA"]
movies = db["Movies"]

def parser(filename):
    doc = open(filename).read()
    jsonObject = json.loads(doc)
    movies.insert_many(jsonObject)
    #print doc

parser("movies.json")
