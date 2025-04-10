import requests

def get_currencys():
    try:
        r = requests.get('http://127.0.0.1:8000')
        currencys = r.json()
        for currency in currencys:
            USD = currency['USD']
        return USD
    except:
        return "Currencys not available"
    
if __name__ == '__main__':
    get_currencys()