import requests
from bs4 import BeautifulSoup

target_url = input("Enter target URL: \n")
print(f'Attempting to get metadata from: {target_url}')

try:
  res = requests.get(target_url)
  res.raise_for_status()
  print("Successfully fetched the page!")
  soup = BeautifulSoup(res.content, 'html.parser')
  print("\n--- HTML Meta Tags found ---")
  meta_tags = soup.find_all('meta')
  
  if not meta_tags:
    print("No <meta> tags found on this page.")
  else:
    for i, tag in enumerate(meta_tags):
      print(f'\nMeta Tag #{i+1}:')
      if tag.get('charset'):
        print(f' Charset: {tag.get("charset")}')
      if tag.get('name'):
        print(f' Name: {tag.get("name")}')
      if tag.get('property'):
        print(f' Property: {tag.get("property")}')
      if tag.get('content'):
        print(f' Content: {tag.get("content")}')
      # print(f' Full tag: {tag}')
except requests.exceptions.RequestException as e:
  print(f'Could not get the URL. Error {e}')
except Exception as e:
  print(f'An unexpected error occurred: {e}')
  
print("\n--- End of Script ---")