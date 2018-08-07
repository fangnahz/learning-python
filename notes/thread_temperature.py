from threading import Thread
import json
from urllib.request import urlopen
import time

CITIES = [
    'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton',
    'Halifax', 'Toronto', 'Charlottetown', 'Regina'
]


class tempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={},CA&units=metric&APPID=e70aff843e9dab2fe27feccbd5ea37bc'
        )
        # See https://openweathermap.org/current for api docs
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']


threads = [tempGetter(c) for c in CITIES]
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()  # wait for the thread to complete before doing anything

for thread in threads:
    print('it is {0.temperature:.0f}°C in {0.city}'.format(thread))
print('Got {} temps in {} seconds'.format(len(threads), time.time() - start))
