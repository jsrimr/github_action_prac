import os
import requests
import pandas as pd

data = pd.read_csv("bitcoin_data.csv")


if __name__ == '__main__':
    event = "github_prac"
    target_url = f'https://maker.ifttt.com/trigger/{event}/with/key/do9TqGuHyqJyXbff2ufCjc'
    requests.post(target_url, data = { "value1" : os.listdir(), "value2":data['c'].head(1).values[0])

