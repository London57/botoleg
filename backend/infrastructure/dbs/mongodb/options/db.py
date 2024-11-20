from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection

import toml


config = toml.load("backend/infrastructure/dbs/mongodb/options/config.toml")

database_config = config.get("mongodb")

url = database_config.get("url")
port = database_config.get("port")

cluster = MongoClient(url, port=port)

businesses_collection: Collection = cluster.botoleg.businesses
