import requests
from bs4 import BeautifulSoup

url = "https://mig.kz/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all('td', class_="buy delta-neutral")
for element in elements:
    print(element.text)
