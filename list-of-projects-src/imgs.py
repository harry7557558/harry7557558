import requests
from io import BytesIO
from PIL import Image
import re
from hashlib import md5

content = open("list-of-projects.md").read()

imgs = re.findall(r"!\[.*?\]\(http.+?\)", content)

MAX_WIDTH = 800
MAX_HEIGHT = 500

for imgsrc in imgs:
    url = re.match(r"!\[.*?\]\((http.+?)\)", imgsrc).group(1)
    print(url)
    r = requests.get(url)
    img = Image.open(BytesIO(r.content)).convert("RGB")
    sc = min(MAX_WIDTH/img.size[0], MAX_HEIGHT/img.size[1])
    if sc < 1.0:
        img = img.resize((int(sc*img.size[0]+0.5), int(sc*img.size[1]+0.5)))
    for c in ['#', '?']:
        url = url[:(url+c).find(c)]
    filename = md5(bytearray(url, 'utf-8')).hexdigest()
    filename = "./list-of-projects-src/" + filename + ".jpg"
    img.save(filename, format="jpeg", optimize=True, quality=85, progressive=True)
    content = content.replace(imgsrc, "![]("+filename+")")
    # break

open("list-of-projects.md", "w").write(content)
