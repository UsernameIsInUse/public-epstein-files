raw = []
confirmed = []
avis = []
unconfirmed = []

with open('videos.txt', "r") as f:
  for url in f:
    if url not in raw:
      raw.append(url)
    
with open('confirmed.txt', "r") as f:
  for url in f:
    if url not in confirmed:
      confirmed.append(url)

with open('avis.txt', "r") as f:
  for url in f:
    if url not in avis:
      avis.append(url)
      
for url in raw:
  if url not in confirmed and url not in avis:
    unconfirmed.append(url)

with open('confirmed.txt', 'w') as f:
  for url in confirmed:
    f.write(url)
    
with open('avis.txt', 'w') as f:
  for url in avis:
    f.write(url)

with open('unconfirmed.txt', 'w') as f:
  for url in unconfirmed:
    f.write(url)