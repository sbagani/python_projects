
import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Otium-Auriculares-inal%C3%A1mbricos-inteligencia-resistente/dp/B07S5JVP78/ref=sr_1_1?dchild=1&keywords=electonics&qid=1590812336&sr=8-1"

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id = "productTitle")
price = soup.find(id="priceblock_ourprice")



print(title)