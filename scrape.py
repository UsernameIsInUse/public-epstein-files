import requests
from fake_useragent import UserAgent

ua = UserAgent()

def write(line:str):
  with open('output.txt', "a") as f:
    f.write(f"{line}\n")

for i in range(1,400):
  n = 0
  while n < 5:
    r = requests.head(f'https://www.justice.gov/multimedia-search?keys=no images produced&page={i}', headers={"User-Agent":ua.random})
    if r.status_code == 200:
      data = r.json()
      try:
        for item in data['hits']['hits']:
          write(item['_source']['ORIGIN_FILE_URI'])
        break
      except:
        write('Item not found')
    n += 1
  if r.status_code != 200:
    write(f'Page {i} - {r.status_code}')
