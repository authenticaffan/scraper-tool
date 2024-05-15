import requests
from bs4 import BeautifulSoup

enter= input("Enter website : ")

req = requests.get(enter)


soup = BeautifulSoup(req.content,"html.parser")

#val = input("Enter what you want to scrap : ")
ss = soup.find('body')
res = ss.get_text()
print(res)