import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://rbtc.live/modlogs/?sub=conspiracy"

r = requests.get(URL)

soup = BeautifulSoup(r.content, features="html.parser")

lis = soup.findAll('div', attrs = {'class':'logcontainer'})

res = []
for container in lis:

    meta = container.find('div', attrs = {'class':'logmeta'})
    time = meta.contents[0]
    # print(f"time: {meta.contents[0]}")

    typ = meta.find('a', attrs = {'title':'View all actions by this type'})
    tp = typ.contents[0]
    # print(f"type: {tp.contents[0]}")

    mod = meta.find('a', attrs = {'title':'View all actions by this mod'})
    moderator = mod.contents[0]
    # print(f"mod: {mod.contents[0]}")

    author = container.find('div', attrs = {'class':'logauthor'})
    auth = author.contents[0].contents[0]
    # print(f"author: {author.contents[0].contents[0]}")

    target = container.find('div', attrs = {'class':'logtarget'})
    tgt = target.contents[0] if target.contents else ''
    # print(f"target: {target.contents[0]}")

    footer = container.find('div', attrs = {'class':'logfooter'})
    foot = footer.contents[0].contents[0] if footer.contents[0].contents else ''

    res.append({'time': time, 'type': tp, 'moderator': moderator, 
                'author': auth, 'target': tgt, 'footer': foot})

res_df = pd.DataFrame(res)
res_df.to_csv(f'data/conspiracy.csv')