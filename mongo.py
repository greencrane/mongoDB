import pymongo

#mongo database stores JSON files.

myclient = pymongo.MongoClient(URL)
print(myclient.list_data_base_names())
mydb = myclient["myDatabase"]
print(mydb.list_collection_names())
mycol = mydb["customers"]

data = { "name": "Tiarnan", "Age": 23}

x = mycol.insert_one(data)

# x = mycol.insert_many(more_data)

