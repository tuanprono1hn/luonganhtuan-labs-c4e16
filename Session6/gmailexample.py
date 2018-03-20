from gmail import GMail, Message
from random import choice
reason = ["MỆT!!!", "BUỒN NGỦ", "MỚI CHIA TAY", "NGƯỜI YÊU ĐI LẤY CHỒNG"]
gmail = GMail("tuanprono1hn1@gmail.com", "linkinpig8494")
# msg = Message("abcef", to = "techkidsc4e16@gmail.com", html = '<h3 class="centeredText"><span color="#e34f26" style="color: #e34f26;"><u>{0}, MAI TAO NGHỈ ĐƯỢC KH&Ocirc;NG???!!!</u></span></h3>'.format(choice(reason)))
msg = Message("abcef", to = "techkidsc4e16@gmail.com", html = '<h3 class="centeredText"><span color="#e34f26" style="color: #e34f26;"><u> {{TAO MỆT}} , MAI TAO NGHỈ ĐƯỢC KH&Ocirc;NG???!!!</u></span></h3>'.replace("{{TAO MỆT}}",choice(reason)))

# placeholder
gmail.send(msg)
