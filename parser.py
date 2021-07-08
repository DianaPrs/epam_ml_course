import requests
import csv

token = "612eeca9a1ea9612e2e309b86f753f78"
#token = "aa32b492b017cb38c892c806ace7601d"
item = "tv-series"
   
with open("srl.txt", 'r') as l:
    data = []
    for link in l.readlines():
        item_id = link.strip()
        link = f"https://api.kinopoisk.cloud/{item}/{item_id}/token/{token}"

        result = requests.get(link)
        
        if result.status_code == 200:
            res = result.json()
            for actor in res["actors"]: 
                data.append({"actor": actor, "title": res["title"]})                   
        else:
            print("Houston, we have a problem!", result.status_code)


with open("data3.csv", 'w', newline='') as f:
    fields = ['actor', 'title']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for row in data:
        writer.writerow(row)            
