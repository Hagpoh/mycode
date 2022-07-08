#!/usr/bin/env python3
"""Alta 3 Flask Final Project
   Patrick Haggerty"""

import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json()

for jedi in resp:
    print(f"{jedi['name']} was a {jedi['age']} year old jedi and had a {jedi['lightsaber color']} lightsaber. They had {len(jedi['apprentices'])} apprentices: {', '.join(jedi['apprentices'])}. They were also known as {jedi['alias']}.\n")
