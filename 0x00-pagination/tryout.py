import requests
import pandas as pd

baseurl = "https://rickandmortyapi.com/api/"
endpoint = 'character'

def main_request(baseurl, endpoint, page):
    r = requests.get(baseurl + endpoint + f'?page={page}')
    return r.json()

def get_pages(resp):
    return resp['info']['pages']

def parse_json(resp):
    charlist = []
    for item in resp['results']:
        char = {
        'id' : item['id'],
        'name' : item['name'],
        'no_ep' : len(item['episode'])
        }
        charlist.append(char)
    return charlist


data = main_request(baseurl, endpoint, 1)

mainlist = []

episodes = data['results'][0]['episode']
for x in range (get_pages(data)):
    mainlist.extend(parse_json(main_request(baseurl, endpoint,x)))

print(len(mainlist))
#print(parse_json(data))

df = pd.DataFrame(mainlist)

df.to_csv('chars.csv', index=False)
