def write(line:str):
  with open('videos.txt', "a") as f:
    f.write(f"{line}")

with open("output.txt", "r") as f:
  for line in f:
    newline = line.replace('.pdf','.mp4')
    write(newline)