import pymongo 

import datetime

import pandas as pd

import stream as stream

s = datetime.date(2021, 8, 9)
e = datetime.date(2021, 9, 9)


# mongodb://localhost:27017/

# if __name__ == "__main__":
#     print()
connection_string=stream.get_connection
# mongodb://localhost:27017/
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client['crypto']
collection_btc = db['btc']
collection_eth = db['eth']
collection_ada = db['ada']
collection_matic = db['matic']
collection_tsla = db['tsla']
collection_sen = db['sen']

# BITCOIN 
def get_all_btc_up():
    items=collection_btc.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5)
    return items

def get_all_btc_low():
    items=collection_btc.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5).sort("_id", pymongo.DESCENDING)
    return items

def get_all_btc_time(start,end):
    items=collection_btc.find({"Date":{ '$gte': start,'$lt':end}},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 })
    return items

# TESLA  
def get_all_tsla_up():
    items=collection_tsla.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5)
    return items

def get_all_tsla_low():
    items=collection_tsla.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5).sort("_id", pymongo.DESCENDING)
    return items

def get_all_tsla_time(start,end):
    items=collection_tsla.find({"Date":{ '$gte': start,'$lt':end}},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 })
    return items

# SENTIMENTAL ANALYSIS 
def get_all_sen(name):
    items=collection_sen.find({"Stocks":name},{"Summary":1,"Label":1,"Confidence":1,"_id":0})
    return items

# Ethereum 
def get_all_eth_up():
    items=collection_eth.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5)
    return items

def get_all_eth_low():
    items=collection_eth.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5).sort("_id", pymongo.DESCENDING)
    return items

def get_all_eth_time(start,end):
    items=collection_eth.find({"Date":{ '$gte': start,'$lt':end}},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 })
    return items

#MATIC 
def get_all_matic_up():
    items=collection_matic.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5)
    return items

def get_all_matic_low():
    items=collection_matic.find({},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 }).limit(5).sort("_id", pymongo.DESCENDING)
    return items

def get_all_matic_time(start,end):
    items=collection_matic.find({"Date":{ '$gte': start,'$lt':end}},{ "Date": 1, "Open": 1,"Close": 1,"High":1,"Low":1,"Volume":1,"_id":0 })
    return items


