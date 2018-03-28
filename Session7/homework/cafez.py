from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html_content = urlopen(url).read().decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("table", id = "tableContent")
tr_list = ul.find_all("tr", ["r_item ", "r_item_a"])
datas = []
for i in tr_list:
    num_list = i.find_all("b_r_c")
    data = {}
    data["Account"] = i.td.string
    data["Quý 4 2016"] = num_list[0].string
    data["Quý 1 2017"] = num_list[1].string
    data["Quý 2 2017"] = num_list[2].string
    data["Quý 3 2017"] = num_list[3].string
    datas.append(data)
print(datas)
