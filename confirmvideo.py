import requests
from fake_useragent import UserAgent

ua = UserAgent()

def write(line:str):
  with open('confirmed.txt', "a") as f:
    f.write(f"{line}\n")

with open("videos.txt", "r") as f:
  for video in f:
    n = 0
    video = video.replace("\n", "")
    while n < 3:
      video = video.replace(".avi", ".mp4")
      r = requests.head(f'{video}', headers={"User-Agent":ua.random}, cookies={'justiceGovAgeVerified':'true'})
      if r.status_code == 200:
        if r.headers['Content-Type'] == "video/mp4":
          write(video)
          print(video)
          break
      elif r.status_code == 404:
        break
