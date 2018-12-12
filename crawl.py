#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

PARSE_URL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

BASE_URL = 'https://www.bing.com'

PIC_INFO = requests.get(PARSE_URL).json()['images'][0]

DATE = PIC_INFO['startdate']
PIC_PATH = PIC_INFO['url']

PIC_URL = BASE_URL + PIC_PATH

response = requests.get(PIC_URL)

with open("~/Pictures/bing-wallpapers/%s.jpg"%DATE, 'wb') as f:
     f.write(response.content)
