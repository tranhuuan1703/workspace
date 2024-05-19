from pymongo import MongoClient


# try:
#     # connection to MongoDB
#     client = MongoClient("mongodb://TranHuuAnAdmin:Admin123@localhost:27017/")

#     # select database
#     db = client["images"]

#     # select collection
#     collection = db['image_information']
# except:
#     print("Can not connection MongoDb database")
path = "mongodb://TranHuuAnAdmin:Admin123@localhost:27017/"
def connection_db(path):
    # connection to MongoDB
    client = MongoClient(path)

    # select database
    db = client["images"]

    # select collection
    collection = db['image_information']

    return collection

print(type(connection_db(path)))