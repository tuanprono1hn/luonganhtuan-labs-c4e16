from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn/"

# # 1. Doenload web page
# # 1.1 Open conntection
# conn = urlopen(url)
# # 1.2 Read
# data = conn.read()
# # print(data)
# # 1.3 decode
# # html_content = data.decode("utf8")
# # print(html_content)

html_content = urlopen(url).read().decode("utf8")

#  save html_content to file
# html_file = open("dantri.html", "wb")
# html_file.write(html_content)
# html_file.close()


# 2. Extract ROI (Regoin of Interest)
soup = BeautifulSoup(html_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew")
# print(ul.prettify())

# 3. Extract Info
li_list = ul.find_all("li")
# for li in li_list:
#     print(li.prettify())
#     print("*" * 30)
datas = []
for li in li_list:
    # li = li_list[0]
    data = {}
    a = li.h4.a
    data["title"] = a.string
    data["link"] = url + a["href"]
    datas.append(data)
pyexcel.save_as(records = datas, dest_file_name = "dantri.xlsx")
