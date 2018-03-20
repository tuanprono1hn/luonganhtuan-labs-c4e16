from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
sum = 0
count_ads = 0
count_wom = 0
count_events = 0
# all_ref = db.customers.find()
# for ref in db.customers.find():
#     print(ref["ref"])
for customer in db.customers.find():
    sum += 1
    if customer["ref"] == "events":
        count_events += 1
    elif customer["ref"] == "ads":
        count_ads += 1
    elif customer["ref"] == "wom":
        count_wom += 1
percent_ads = count_ads/sum *100
percent_wom = count_wom/sum *100
percent_events = count_events/sum *100
labels = ["ads","wom","events"]
values = [count_ads, count_wom, count_events]
colors = ["red","green","blue"]
pyplot.pie(values, labels = labels, colors = colors)
pyplot.axis("equal")
pyplot.show()
