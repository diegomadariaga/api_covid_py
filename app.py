# -*- coding: UTF-8 -*-
import requests


def conectApi(url):
    response = requests.get(url)
    if response.status_code == 200:
        # print response
        print(response.json()['name'])
        return response.json()
    else:
        return None

conectApi('https://pokeapi.co/api/v2/pokemon/1')
