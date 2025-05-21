import requests
from bs4 import BeautifulSoup
import json

def scrape():
  url = "https://bykea.com/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  print(soup)
  
if __name__ == '__main__':
  scrape()