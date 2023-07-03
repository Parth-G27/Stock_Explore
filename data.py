import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import regex as re
sns.set_theme()

# change the connection string
client = pymongo.MongoClient(
    "mongodb+srv://parth3_mongo:parthdb48@cluster1.sqvug29.mongodb.net/")
print(client)
db = client['Stock_Explore']  # crypto --> Stock_Explore
collection_btc = db['btc']
collection_eth = db['eth']
cursor_btc = collection_btc.find()
cursor_eth = collection_eth.find()
entries_btc = list(cursor_btc)
entries_eth = list(cursor_eth)
# print(entries_btc[:5])
df_btc = pd.DataFrame(entries_btc)
df_eth = pd.DataFrame(entries_eth)

# print(df_btc)
# print(df_eth)

# ---------------------------------------------------
btc_time = pd.DataFrame(df_btc['Date'])
eth_time = pd.DataFrame(df_eth['Date'])
btc_time['Date']=resub(r"-","/",btc_time['Date'])
eth_time['Date']=resub(r"-","/",eth_time['Date'])
btc_time['Date'] = btc_time['Date'].astype('datetime64[ns]')
eth_time['Date'] = eth_time['Date'].astype('datetime64[ns]')
df_btc['Close'] = df_btc['Close'].astype('Float32')
df_eth['Close'] = df_eth['Close'].astype('Float32')
print(btc_time['Date'])
# print(eth_time['Date'])

print(df_btc['Close'])
# print(df_eth['Close'])

print('stage')

plt.plot(btc_time['Date'], df_btc['Close'])
# plt.plot(eth_time['Date'],df_eth['Close'])
plt.show()

print('Running ....')

# ---------------------------------------------------

# DD/MM/YYYY

# DD-MM-YYYY
