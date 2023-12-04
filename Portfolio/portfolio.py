from Portfolio.hashmap import HashMap

class Portfolio:
    def __init__(self):
        self.map = HashMap()

    def add_investment(self, ticker, company_name, shares, value_usd, purchase_price,  purchase_date):
        details = {
            'Company Name': company_name,
            'Ticker': ticker,
            'Shares': shares,
            'Value Usd': value_usd,
            'Purchase Price': purchase_price,
            'Purchase Date': purchase_date
        }
        self.map.insert(ticker, details)

    def remove_investment(self, ticker):
        self.map.delete(ticker)

    def get_investment(self, ticker):
        self.map.get(ticker)

    
