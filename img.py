import random 
import pickle
import json
from bs4 import *
import request 
import os

r2 = rq.get("https://www.reddit.com/r/food/")
food_reddit = BeautifulSoup(r2.text, "html.parser")

links = []

extract = food_reddit.select('img[src^="https://i.reddit.it/.jpg"]')

for jpg in extract:
    links.append(img['src'])

for l in links:
    print(l)