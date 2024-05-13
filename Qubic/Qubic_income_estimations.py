#EPOCH 101 hashrates updated! See link above.
#enter you total hashrate of your rigs here (in it/s)
myHashrate = 118



#doing the math
import sys
#!{sys.executable} -m pip install pycoingecko
import requests
import json
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI

print('\n\n Введите Ваш Hashrate:')
myHashrate = float(input())

rBody = {'userName': 'guest@qubic.li', 'password': 'guest13@Qubic.li', 'twoFactorCode': ''}
rHeaders = {'Accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
r = requests.post('https://api.qubic.li/Auth/Login', data=json.dumps(rBody), headers=rHeaders)
token = r.json()['token']
rHeaders = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
r = requests.get('https://api.qubic.li/Score/Get', headers=rHeaders)
networkStat = r.json()

epochNumber = networkStat['scoreStatistics'][0]['epoch']
epoch97Begin = date_time_obj = datetime.strptime('2024-02-21 12:00:00', '%Y-%m-%d %H:%M:%S')
curEpochBegin = epoch97Begin + timedelta(days=7 * (epochNumber - 97))
curEpochEnd = curEpochBegin + timedelta(days=7) - timedelta(seconds=1)
curEpochProgress = (datetime.utcnow() - curEpochBegin) / timedelta(days=7)

netHashrate = networkStat['estimatedIts']
netAvgScores = networkStat['averageScore']
netSolsPerHour = networkStat['solutionsPerHour']

crypto_currency = 'qubic-network'
destination_currency = 'usd'
cg_client = CoinGeckoAPI()
prices = cg_client.get_price(ids=crypto_currency, vs_currencies=destination_currency)
qubicPrice = prices[crypto_currency][destination_currency]
poolReward = 0.85
incomerPerOneITS = poolReward * qubicPrice * 1000000000000 / netHashrate / 7 / 1.06
curSolPrice = 1479289940 * poolReward * curEpochProgress * qubicPrice / (netAvgScores * 1.06)


print('\n\nИнформация о текущей эпохе:')
print('Текущая эпоха:',  epochNumber)
print('Старт Эпохи UTC:',  curEpochBegin)
print('Конец Эпохи UTC:',  curEpochEnd)
print('Прогресс Эпохи:',  '{:.1f}%\n'.format(100 * curEpochProgress))
print('Информация о Сети:')
print('Предполагаемый сетевой хэшрейт:', '{0:,}'.format(netHashrate).replace(',', ' '), 'it/s')
print('Средний счет:',  '{:.1f}'.format(netAvgScores))
print('Баллов в час:',  '{:.1f}\n'.format(netSolsPerHour))
print('Оценка дохода:')
print('При использовании пула с фиксированным вознаграждением в размере 85%\n')
print('Цена на кубик: {:.8f}$'.format(qubicPrice))
print('Предполагаемый доход на 1 it/с в день:', '{:.4f}$\n'.format(incomerPerOneITS))
print('Ваш предполагаемый доход в день:', '{:.2f}$'.format(myHashrate * incomerPerOneITS))
print('Предполагаемый доход на 1 сол:', '{:.2f}$'.format(curSolPrice))
print('Предполагаемый доход, который вы получаете в день:', '{:.1f}\n\n'.format(24 * myHashrate * netSolsPerHour / netHashrate))