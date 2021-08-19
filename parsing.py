import requests
from bs4 import BeautifulSoup
import json


URL = "http://www.kenesh.kg/ru/deputy/list/35?page=3"
HEADERS = {
         "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
         (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", 
        #  "accept":"*/*", 
}


PATH = "parse.json"

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)

    return r

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="dep-item")
    print(items)
    komp = []
    for item in items:
        print(item)
        komp.append({
            "name": item.find("a", class_="name").get_text(),
            "info":item.find("div", class_="info").get_text(),
            "tel": item.find("div", class_="bottom-info").get_text(),
            "image" : item.find("a").get("href"),
        }
        )
       
    print(komp)
    return komp



def save_json(items, path):
    with open(path, 'w') as f:
        jsonData = json.dumps(items, ensure_ascii=False, indent=4)
        f.write(jsonData)
        print(jsonData)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        komps = get_content(html.text)
        save_json(komps, PATH)
        print(komps)
       

    else:
        print("error not connect")



parse()
