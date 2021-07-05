import requests
import csv

#token = "612eeca9a1ea9612e2e309b86f753f78"
token = "aa32b492b017cb38c892c806ace7601d"
item = "tv-series"

with open("data.csv", 'w', newline='') as f:
    fields = ['title', 'actor']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    data = []
    
    with open("srl.txt", 'r') as l:
      
        for link in l.readlines():
            item_id = link.strip()
            link = f"https://api.kinopoisk.cloud/{item}/{item_id}/token/{token}"

            result = requests.get(link)
            
            if result.status_code == 200:
                res = result.json()
                for actor in res["actors"]: 
                    data.append({"title": res["title"], "actor": actor})                   
            else:
                print("Houston, we have a problem!", result.status_code)

        for row in data:
            writer.writerow(row)            
