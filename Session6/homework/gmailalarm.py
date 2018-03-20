from gmail import GMail, Message
# from random import choice
import datetime
gmail = GMail("tuanprono1hn1@gmail.com", "linkinpig8494")
msg = Message("Call in sick", to = "techkidsc4e16@gmail.com", text = "I'm sick. I'm sending this mail for asking for a day off")
now = datetime.datetime.now()
while True:
    if now.hour == 7:
        gmail.send(msg)
        break
