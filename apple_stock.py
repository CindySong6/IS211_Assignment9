# Scraping data of Apple Stocks on Yahoo Finance
# https://finance.yahoo.com/quote/AAPL/history?p=AAPL
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
page= requests.get(url=URL, headers=headers)
soup = BeautifulSoup(page.content, 'html5lib')

# # display the apple stocks table header
print("Date\t\t\tOpen\t\tHigh\t\tLow\t\tClose*\t\tAdj Close**\t\tVolume")
print('\n')

# display the apple stocks table data
apple_stocks_data = soup.findAll('tr', attrs={"class":"BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"})
for datarow in apple_stocks_data:
    for data in datarow:
        print(data.text, end="\t\t")
    print('\n')

if __name__ == "__main__":
    pass
