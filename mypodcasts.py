import getpodcast

opt = getpodcast.options(
    date_from='2023-01-01',
    root_dir='./podcast')

podcasts = {
    'resetnyc': 'https://feeds.buzzsprout.com/767921.rss'}


getpodcast.getpodcast(podcasts, opt)

# import requests
# import os

# def download_episode(url, filename):
#     """
#     Downloads an Apple Podcast episode given a URL to the audio file and a desired filename.
#     """
#     response = requests.get(url, stream=True)
#     if response.status_code != 200:
#         print(f"Error: Unable to download episode ({response.status_code})")
#         return

#     with open(filename, "wb") as f:
#         for chunk in response.iter_content(chunk_size=1024):
#             f.write(chunk)

#     print(f"Episode downloaded to {os.path.abspath(filename)}")


# url = "https://podcasts.apple.com/us/podcast/0222-%E6%99%AE%E4%B8%81%E6%9A%AB%E9%80%80%E9%99%90%E6%AD%A6%E6%A2%9D%E7%B4%84%E6%81%A2%E5%BE%A9%E6%A0%B8%E8%A9%A6%E7%88%86-%E4%B8%AD%E5%9C%8B%E4%B8%8D%E6%99%AF%E6%B0%A3%E5%8E%BB%E5%B9%B4%E6%B3%95%E6%8B%8D%E5%B1%8B60%E8%90%AC%E6%88%B6%E5%89%B5%E6%96%B0%E9%AB%98-%E6%97%A5%E6%9C%AC%E9%AB%98%E9%9A%8E%E5%A4%96%E5%9C%8B%E4%BA%BA%E6%89%8D66-%E4%BE%86%E8%87%AA%E4%B8%AD%E5%9C%8B/id1558410138?i=1000601022159"
# filename = "newsepisode.mp3"

# download_episode(url, filename)