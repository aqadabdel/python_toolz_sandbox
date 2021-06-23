from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


site= "https://www.coinwarz.com/mining/bitcoin/hashrate-chart"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
 
btc_ath = 64863
btc_curr_price = 34211

span = soup.find_all('span', class_="font-38 bold muted")
btc_curr_hashrate = span[0].get_text().replace('EH/s','').strip()
btc_ath_hashrate = span[1].get_text().replace('EH/s','').strip()

btc_ath_hashrate = round(float(btc_ath_hashrate))
print(btc_ath_hashrate)

btc_hash_ratio = btc_ath / btc_ath_hashrate
btc_fair_price = btc_curr_hashrate * btc_curr_price



print(f'Current Hashrate: {btc_curr_hashrate} EH/s')
print(f'ATH Hashrate: {btc_ath_hashrate} EH/s' )
#print(f'BTC Fair Price: {btc_fair_price} $' )