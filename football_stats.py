# Scraping data of CBS NFL Players and Display top 20 NFL players ranked by number of touchdown
# https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
URL = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
page= requests.get(url=URL, headers=headers)
soup = BeautifulSoup(page.content, 'html5lib')

table = soup.findAll('tr', attrs={'class':'TableBase-bodyTr'})

# print header
print("""
Top 20 NFL players ranked by Touchdowns
Player Name\t\tPosistion\tTeam\tTotal Number of Touchdown
------------------------------------------------------------------------------
""")

# print data
for row in table[0:20]:
    player_name_info = row.find('span', attrs={'class':'CellPlayerName--long'})
    player_name = player_name_info.a.text
    player_position = player_name_info.find('span', attrs='CellPlayerName-position').text.strip()
    player_team = player_name_info.find('span', attrs='CellPlayerName-team').text.strip()
    total_touchdowns = row.findAll('td', 'TableBase-bodyTd TableBase-bodyTd--number')[7].text.strip()
    print(f"{player_name}\t\t{player_position}\t\t{player_team}\t\t{total_touchdowns}")

if __name__ == "__main__":
    pass
