'''
Financial Modeling Prep is a new concept that informs you about stock markets information (news, currencies and stock prices).
This organization runs a free api that we will read data in from
'''

from urllib.request import urlopen
import json
from pandas import DataFrame

def get_jsonparsed_data(ticker):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    url = get_url(ticker)
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_url(ticker):
    url = 'https://financialmodelingprep.com/api/financials/income-statement/' + ticker + '?datatype=json'
    return url

def get_company_dataframe(ticker):
    '''
    this is just a bonus :)
    '''
    data = get_jsonparsed_data(ticker)
    df = DataFrame(data[ticker])
    return df

ticker = 'FB'

print("JSON:")
data = get_jsonparsed_data(ticker)
print(data)

print('\nthat\'s hard to read... let\'s try a dataframe:')
data = get_company_dataframe(ticker)
print(data.head())
