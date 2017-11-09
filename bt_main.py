# -*- coding: utf-8 -*-
import requests
# import os
import config
import json
import time
import schedule
from bs4 import BeautifulSoup
import telegram_module
"""
		
def regalcoin():
	coins = requests.get("https://api.coinmarketcap.com/v1/ticker/regalcoin").json()
	for i in coins:
		if i["id"] == "regalcoin":
			sms2 = "---------\n"+ i['symbol'] + ': '+'$ '+ i['price_usd']+" ("+i['percent_change_24h']+"%)"
			b=telegram_module.telegram_send_to(config.chat_id,sms2,config.api_telegram)
#def rega():
#    url = 'https://coinmarketcap.com/currencies/regalcoin/'
#    res = BeautifulSoup(requests.get(url).text, 'lxml')
#    rega = res.find('div', attrs={'class':'col-xs-6 col-sm-8 col-md-4 text-left'}).text.strip()
#    sms3 = '---------\n REC: '+rega
#    b=telegram_module.telegram_send_to(config.chat_id,sms3,config.api_telegram)
"""
"""def get_coins_info():
	coins = requests.get("https://api.coinmarketcap.com/v1/ticker/").json()
	sms = []
	for i in coins:
		if i["id"] in ["bitconnect", "electroneum", "bitcoin"]:
			sms.append("Gia " + i['symbol'] + ': '+'$ '+ i['price_usd']+" ("+i['percent_change_24h']+"%)")
	telegram_module.telegram_send_to(config.chat_id,'\n'.join(sms),config.api_telegram)
"""
def get_coins_info():
	coins = ["bitcoin", "bitconnect", "electroneum", "regalcoin"]
	sms = []
	for coin in coins:
		res = requests.get("https://api.coinmarketcap.com/v1/ticker/"+coin).json()[0]
		sms.append("" + res['symbol'] + ': '+'$ '+ res['price_usd']+" ("+res['percent_change_24h']+"%)")
	telegram_module.telegram_send_to(config.chat_id,'\n'.join(sms),config.api_telegram)
def increase():
    global client
    url = 'https://bitconnect.co/learning-center/bitconnect-bitcoin-price-volatility-software/'
    data = BeautifulSoup(requests.get(url).text, 'lxml').find('div', attrs={'class':'row pricechart'})
    percents = data.findAll('div', attrs={'class': None})
    message2 = 'Chao ban, lai hom nay la: '+percents[0].text
    b=telegram_module.telegram_send_to(config.chat_id,message2,config.api_telegram)
#getbitcoin()
get_coins_info()
#b=telegram_module.telegram_send_to(config.chat_id,abc,config.api_telegram)
#regalcoin()
#rega()
schedule.every(1).minutes.do(get_coins_info)
#schedule.every(5).minutes.do(electroneum)
#schedule.every().day.at("17:01").do(increase)
if __name__ == '__main__':
	while True:
		try:
			schedule.run_pending()
			#bitconnect()
			#electroneum()
			
		except Exception as value:
			print(value)
			pass
