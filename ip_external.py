import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
response = urlopen(url)

dados = json.load(response)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

print(f'Details from External IP')
print('-' * 24)
print(f'Org: {org}\nRegion: {region}\nCountry: {country}\nCity: {city}\nIP: {ip}')
