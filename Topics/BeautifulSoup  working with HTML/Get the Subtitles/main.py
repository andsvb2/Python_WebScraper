import requests

from bs4 import BeautifulSoup

# Examples
# index = 1
# url = "https://www.grammarly.com/blog/articles/"

index = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

subtitles = soup.find_all('h2')
print(subtitles[index].text)
