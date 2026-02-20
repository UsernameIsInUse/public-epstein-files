import requests
from fake_useragent import UserAgent

ua = UserAgent()

def write(line:str):
  with open('othertypes.txt', "a") as f:
    f.write(f"{line}\n")
    
unconfirmed = []

with open('unconfirmed.txt', "r") as f:
  for video in f:
    unconfirmed.append(video.replace("\n", ""))

print(len(unconfirmed))

def check(url:str,type:str,format:str,filetype=None):
  n = 0
  found = False
  if not filetype:
    filetype = format
  url = url.replace('.mp4',f'.{format}')
  while n < 2:
    r = requests.head(url, headers={"User-Agent":ua.random}, cookies={'justiceGovAgeVerified':'true'})
    if r.status_code == 200:
      if r.headers['Content-Type'] == f"{type}/{filetype}":
        print(f"found {format}")
        write(url)
        print(url)
        found = True
        break
    elif r.status_code == 404:
      break
  return found
  
for url in unconfirmed:
  print(f'checking {url}')
  notFound = True
  """
  # videos
  if notFound and check(url,"video","avi"):
    notFound = False
  elif notFound and check(url,"video","mpeg"):
    notFound = False
  elif notFound and check(url,"video","webm"):
    notFound = False
  """
  #images
  if notFound and check(url,"image","jpeg"):
    notFound = False
  elif notFound and check(url,"image","gif"):
    notFound = False
  elif notFound and check(url,"image","png"):
    notFound = False
  elif notFound and check(url,"image","tiff"):
    notFound = False
  elif notFound and check(url,"image","webp"):
    notFound = False
  """
  #audio
  elif notFound and check(url,"audio","mp3"):
    notFound = False
  elif notFound and check(url,"audio","wav"):
    notFound = False
  elif notFound and check(url,"audio","weba","webm"):
    notFound = False
  
  
  #zip
  elif notFound and check(url,"application","x-7z-compressed"):
    notFound = False
  elif notFound and check(url,"application","rar","vnd.rar"):
    notFound = False
  elif notFound and check(url,"application","zip"):
    notFound = False
  elif notFound and check(url,"application","zip","x-zip-compressed"):
    notFound = False
    
  #doc
  elif notFound and check(url,"text","csv"):
    notFound = False
  elif notFound and check(url,"application","doc","msword"):
    notFound = False
  elif notFound and check(url,"application","docx","vnd.openxmlformats-officedocument.wordprocessingml.document"):
    notFound = False
  elif notFound and check(url,"application","docx","vnd.openxmlformats-officedocument.wordprocessingml.document"):
    notFound = False
  elif notFound and check(url,"application","json"):
    notFound = False
  elif notFound and check(url,"application","md"):
    notFound = False
  elif notFound and check(url,"application","ppt","vnd.ms-powerpoint"):
    notFound = False
  elif notFound and check(url,"application","pptx","vnd.openxmlformats-officedocument.presentationml.presentation"):
    notFound = False
  elif notFound and check(url,"application","txt"):
    notFound = False
  elif notFound and check(url,"application","xml"):
    notFound = False
  """