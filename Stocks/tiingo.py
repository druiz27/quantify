import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 66e0bf2887d62ab992c42009916b3ebb8dce4276'
}


def get_meta_deta(ticker):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}"
    response = requests.get(url, headers=headers)
    return response.json()


def get_price_data(ticker):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    response = requests.get(url, headers=headers)
    print("API Response:", response.text)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

