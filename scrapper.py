from bs4 import BeautifulSoup
import requests
import csv

# Receive all content of HTTP request
site = requests.get('https://www.climatempo.com.br/').content

# Get the HTML code
soup = BeautifulSoup(site, 'html.parser')

header = ['Link label', 'Link destination']
print(f'Generating CSV file of all links')
with open('links.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(header)
    links = soup.findAll('a', class_='link actTriggerGA', href=True)
    for link in links:
        write.writerow([link.string, link['href']])

print(f'CSV file has been created successfully')
