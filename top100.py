from bs4 import BeautifulSoup

with open('kino', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

try:
    links = soup.find_all("a")
    for link in links:
        link.get('href')
    with open('srl', 'r') as f:
        for line in f.readlines():
            print(line.strip())
except Exception as ex:
    print(f"Fail {ex}")