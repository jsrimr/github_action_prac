import os
import requests

if __name__ == '__main__':
    event = "github_prac"
    target_url = f'https://maker.ifttt.com/trigger/{event}/with/key/do9TqGuHyqJyXbff2ufCjc'
    requests.post(target_url, data = { "value1" : os.listdir()})

