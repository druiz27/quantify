from .portfolio import Portfolio
from django.shortcuts import render
from .forms import InvestmentForms

def investment_interface(request):
    if request.method == 'POST':
        form = InvestmentForms(request.POST)
        if form.is_valid():
            # retrieve data from form
            ticker = form.cleaned_data['ticker']
            company_name = form.cleaned_data['company_name']
            shares = form.cleaned_data['shares']
            value_usd = form.cleaned_data['value_usd']
            purchase_price = form.cleaned_data['purchase_price']
            purchase_date = form.cleaned_data['purchase_date']

            # create instance of portfolio and add user input to it
            portfolio = Portfolio().add_investment(ticker, company_name, shares, value_usd)
    else:
        form = InvestmentForms()

    return render(request, 'Portfolio/investment_interface.html', {'form': form})

