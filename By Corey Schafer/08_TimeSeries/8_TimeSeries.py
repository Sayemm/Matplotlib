import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta

plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#
# y = [0, 1, 3, 4, 6, 5, 7]
#
# plt.plot_date(dates, y, linestyle = 'solid') #linestyle = line plot (solid)
# plt.gcf().autofmt_xdate() #get current figure
#
# date_format = mpl_dates.DateFormatter('%b, %d, %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

df = pd.read_csv('timeseries_data.csv')
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace = True)

price_date = df['Date']
price_close = df['Close']

plt.plot_date(price_date, price_close, linestyle = 'solid')
plt.gcf().autofmt_xdate() #rotate date

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.savefig('8_TimeSeries.png')
plt.show()