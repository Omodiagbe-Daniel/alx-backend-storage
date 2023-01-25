#!/usr/bin/env python3
"""Python script that provides some stats
   about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.nginx
    no_doc = (collection.count_documents({}))
    print(f"{no_doc} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for meth in methods:
        res = collection.count_documents({"method": meth})
        print("\tmethod {}: {}".format(meth, res))
    rest = collection.count_documents({"path": "/status"})
    print("{} status check".format(rest))
