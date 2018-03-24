from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen(url).read().decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")
listdiv = soup.find_all("div", "section-content")
li_list = listdiv[1].find_all("li")
chart = []
for li in li_list:
    song = {}
    pos = li.strong.string
    name = li.h3.string
    artist = li.h4.string
    song["Rank"] = pos
    song["Name"] = name
    song["Artist"] = artist
    chart.append(song)
pyexcel.save_as(records = chart, dest_file_name = "iTunesTopSongs.xlsx")
options = {
    "default_search" : "ytsearch",
    "max_downloads" : 2
    }
dl = YoutubeDL(options)
download_list = []
for i in chart:
    download_list.append(i["Name"] + i["Artist"])
dl.download(download_list)
# print(download_list, sep = "\n")
