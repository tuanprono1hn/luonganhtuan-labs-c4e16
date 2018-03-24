from youtube_dl import YoutubeDL
# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=lGbzyKWkiio']) # Remember to put your video in a list, eventhough one video is downloaded



# Sample 2: Download multiple youtube videos
# Put list of song urls in download function to download them, one by one
dl.download(['https://www.youtube.com/watch?v=4vNZq5U1PmY', 'https://www.youtube.com/watch?v=eiDiKwbGfIY'])



# Sample 3: Download audio
options = {
    'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=eiDiKwbGfIY'])



# Sample 4: Search and then download the first video
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['Thinking Out Loud Ed Sheeran'])


# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Tạm biệt'])
