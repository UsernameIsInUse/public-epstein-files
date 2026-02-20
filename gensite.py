import glob
from dominate import document
from dominate.tags import *
from dominate.util import raw

doc = document(title='epstein video list')

with doc.head:
  meta(name='viewport',content='width=device-width, initial-scale=1, shrink-to-fit=no')

with doc:
  h1('mp4s')
  with div().add(ol()):
    with open("confirmed.txt", "r") as f:
      for url in f:
        url = url.replace("\n", "")
        li(a(url, href=url))
  h1('avis')
  p('these will download directly to your device')
  with div().add(ol()):
    with open("avis.txt", "r") as f:
      for url in f:
        url = url.replace("\n", "")
        li(a(url, href=url))

with open('index.html', 'w') as f:
    f.write(doc.render())