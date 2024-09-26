import datetime
import requests

time1 = datetime.date(1995, 6, 16)
time2 = datetime.date(1996, 6, 17)
url = "https://api.nasa.gov/planetary/apod"



t1 = time1
nod = 0
while t1 != time2:
    print(t1)
    r = requests.get(url, params={'api_key': 'oe5Fxi2bg0QUgh11QBackdf0YtnfeXtJqysSU1sk', 'date': t1.strftime('%Y-%m-%d')})
    print(r.status_code)
    if r.status_code == 200:
        nod += 1
    t1 += datetime.timedelta(days=1)
    print(nod)

print(f'Всего записей за этот период - {nod}')