from lxml import html
import requests
# import nordypy
import pandas as pd
from pandas.io.json import json_normalize
from pandas import DataFrame
import urllib2
from bs4 import BeautifulSoup

## fantasy rosters
response = requests.get('http://fantasy.espn.com/baseball/league/rosters?leagueId=96224')
soup = BeautifulSoup(response.text, "html.parser")

name_box = soup.find('span', attrs={'class': 'teamName truncate'})
name_box
#espn-analytics > div > div.jsx-813185768.shell-container > div.page-container.cf
# > div.layout.is-full > div >
#div.jsx-2320949408.league-rosters-tables > div > div:nth-child(1) > div >
#div.jsx-3572281990.rosterTable

rows = soup.find_all('.league-rosters-tables')
rows
#<span title="Larry Bernandez" class="teamName truncate">Larry Bernandez</span>
#//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section


tree = html.fromstring(response.content)

#This will create a list of players:
buyers = tree.xpath('//div[@.league-rosters-tables]"]/text()')
buyers
