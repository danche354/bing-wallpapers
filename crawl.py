#!/anaconda2/bin/python
# -*- coding: utf-8 -*-

import requests

PARSE_URL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8'

BASE_URL = 'https://www.bing.com'

for i in range(8):
    PIC_INFO = requests.get(PARSE_URL).json()['images'][i]

    DATE = PIC_INFO['startdate']
    PIC_PATH = PIC_INFO['url']

    PIC_URL = BASE_URL + PIC_PATH

    print PIC_URL
    response = requests.get(PIC_URL)

    with open("~/Pictures/bing-wallpapers/%s.jpg"%DATE, 'wb') as f:
         f.write(response.content)
