from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

ID_APP = 'TaseenSi-eba-PRD-cc5c26cd1-8b1f1867'

Keywords = input('what are you searching for?\n')
api = finding(appid=ID_APP, config_file=None)
api_request = { 'keywords': Keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    print('________')
    print('category: ' + cat + '\n')
    print('title: ' + title + '\n')
    print('price: $' + str(price) + '\n')
    print('url: ' + url + '\n')
    input()

