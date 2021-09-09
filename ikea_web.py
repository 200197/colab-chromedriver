import requests
from bs4 import BeautifulSoup

URL = "https://www.ikea.com.hk/zh/products/sofas-and-armchairs/armchairs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="productList")
#print(results)

items = results.find_all("div", class_= "itemInfo")
#print(names)

for item in items:
  oldprice = item.find("p", class_="itemOldPrice")
  price = item.find("div", class_="itemPrice-wrapper")
  name = item.find("div", class_="itemDetails")
  type = item.find("h6", class_="display-7")

  print(oldprice)
  print(name.text.strip())
  print(price.text.strip())
  print(type.text.strip())
