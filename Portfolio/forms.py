from django import forms

class InvestmentForms(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)
    company_name = forms.CharField(label='Company Name')
    shares = forms.CharField(label='Shares')
    value_usd = forms.CharField(label='Value (USD)')
    purchase_price = forms.CharField(label='Purchase')
    purchase_date = forms.CharField(label='Purchase Date')
