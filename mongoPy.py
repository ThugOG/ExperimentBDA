import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient.drop_database("starlight")
mydb = myclient["starlight"]
mycol = mydb["orders"]
# New col
print("Initial Query: Created Col")
for x in mycol.find():
    print(x)
print("")
mylist = [
{ "_id": 1, "cust_id": "Anya Forger",  "spent": 25 },
{ "_id": 2, "cust_id": "Anya Forger",  "spent": 70 },
{ "_id": 3, "cust_id": "Bakugo Katsuki",  "spent": 50 },
{ "_id": 4, "cust_id": "Bakugo Katsuki",  "spent": 25 },
{ "_id": 5, "cust_id": "Bakugo Katsuki",  "spent": 50 },
{ "_id": 6, "cust_id": "Candice Knots",  "spent": 35 },
{ "_id": 7, "cust_id": "Candice Knots",  "spent": 25 },
{ "_id": 8, "cust_id": "Dabi Todoroki",  "spent": 75 },
{ "_id": 9, "cust_id": "Dabi Todoroki",  "spent": 50 },
{ "_id": 11, "cust_id": "All Might",  "spent": 50 }
]
# Insert multiple records into MongoDB
mycol.insert_many(mylist)
print("Insert Multiple Records:")
for x in mycol.find():
    print(x)
print("")
# Insert single record into MongoDB
mycol.insert_one({ "_id": 10, "cust_id": "Dabi Todoroki",  "spent": 25 })
print("Insert Single Record")
for x in mycol.find():
    print(x)
print("")
# Delete a record from MongoDB
mycol.delete_one( { "cust_id": "All Might" } )
print("Delete Single Record")
 
for x in mycol.find():
    print(x)
print("")
# Find a record from MongoDB
print("Search Query")
for x in mycol.find({ "_id": 3}):
    print(x)
print("")
# Update a record from MongoDB
mycol.update_one( { "_id": 3}, { "$set": { "cust_id": "Anya Forger" } })
print("Update Single Record")
for x in mycol.find():
    print(x)
print("")
# Map reduce query to find total money spent by a customer
pipeline = [
      { "$group": {
       "_id": "$cust_id",
       "spent": { "$sum": "$spent" }
       }
      },
      { "$project": {
      "Name": "$_id",
      "spent": 1,
      "_id": 0
      }
      },
      { "$sort": {
"Name": 1 }
} ]
result = list(mycol.aggregate(pipeline))
print("Map Reduce using MongoDB")
# Manually print fields in the desired order
for doc in result:
      print("Name:", doc.get("Name"), end="\t")
      print("Total Spent:", doc.get("spent"))
