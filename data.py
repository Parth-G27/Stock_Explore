import pymongo 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client['crypto']
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

btc_time=pd.DataFrame(df_btc['Date'])
eth_time=pd.DataFrame(df_eth['Date'])

print(btc_time['Date'])
# print(eth_time['Date'])

print(df_btc['Close'])
# print(df_eth['Close'])

print('stage')

plt.plot(btc_time['Date'],df_btc['Close'])
# plt.plot(eth_time['Date'],df_eth['Close'])
plt.show()

print('Running ....')