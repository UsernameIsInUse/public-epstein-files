import glob
from dominate import document
from dominate.tags import *

doc = document(title='epstein video list')

with doc:
  h1('videos')
  with div().add(ol()):
    with open("confirmed.txt", "r") as f:
      for video in f:
        video = video.replace("\n", "")
        li(a(video, href=video))

with open('index.html', 'w') as f:
    f.write(doc.render())