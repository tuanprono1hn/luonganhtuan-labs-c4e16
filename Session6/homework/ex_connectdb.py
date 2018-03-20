from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
new_post = {
    "title" : "Hễ đi là đến",
    "author" : "Tuấn Tồ",
    "content" : str("Cảm nghĩ gì về C4E á? hmm... Nó khá vui đó chứ, nhưng có vẻ thời gian giành cho nó chưa thực sự hợp lý làm mình có cảm giác tụt lùi so với các bạn trẻ bây giờ :)) Còn về title thì do nhiều lúc tự nghĩ sẽ thế nào khi mình cứ làm hết những thứ mà người khác muốn mình làm; trở thành người mà mọi người muốn mình trở thành? Nhưng cuối cùng mình vẫn giữ được suy nghĩ rằng mỗi người sinh ra đều đã có đích đến của riêng mình rồi thì đi con đường nào rồi cũng sẽ đến được đó thôi >:)"),
    }
db.posts.insert_one(new_post)
