import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
url = 'https://www.newegg.ca/p/pl?d=macbook'

# open connection and grap the page
u_client = uReq(url)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html, "html.parser")
all_item_containers = page_soup.findAll('div', {'class': 'item-container'})
filename = 'product.csv'
file = open(filename, "w")
header = "brand,title,price,shipping\n"
file.write(header)
seperator = '|'
for index in range(4, len(all_item_containers)):
	item_container = all_item_containers[index]
	title = item_container.find('a', {'class': 'item-title'}).text
	item_action_div = item_container.find('div', {'class': 'item-action'})
	current_price_li = item_action_div.find('li', {'class': 'price-current'})
	price_dollar = current_price_li.strong.text.replace(',', '')
	price_cent = current_price_li.sup.text
	current_price = price_dollar + price_cent

	shipping_info = item_action_div.find('li', {'class': 'price-ship'}).text.strip()
	print(shipping_info)
	item_brand = item_container.find('a', {'class', 'item-brand'})
	if not item_brand:
		brand = ""
	else:
		if item_brand.img == None:
			brand = ""
		else:
			brand = item_brand.img['title']
	file.write(brand + ',' + title.replace(',', '-') + ',' + current_price + ',' + shipping_info + '\n')
file.close()