import pandas as pd
import random
import json
import math
import time
import datetime

from pandas import datetime
from pandas_datareader import data

print('Enter a NYSE ticker symbol:')
stock = input() #asks for input

start = datetime(2016,3,19)
end = datetime(2018,3,26)

df = data.DataReader(stock, 'iex', start, end)
print(df.head())
print(df.tail())
