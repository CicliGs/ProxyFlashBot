import json
import requests

from config_reader import config

url = 'https://api.oxapay.com/merchants/inquiry'


def payment_details(track_id: int):
    data = {
        "merchant": config.oxapay_merchant_key.get_secret_value(),
        "trackId": track_id
    }

    response = requests.post(url=url, data=json.dumps(data))

    res = response.json()

    if res["result"] == 100:
        print("Oxapay responsed succesfully")
        return res
    print(f"Oxapay says that result is {res['result']}")
    return None
