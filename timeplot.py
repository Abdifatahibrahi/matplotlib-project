import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta, date


plt.style.use('seaborn')


# dates = [
#     datetime(2020, 6, 1),
#     datetime(2020, 6, 2),
#     datetime(2020, 6, 3),
#     datetime(2020, 6, 4),
#     datetime(2020, 6, 5),
#     datetime(2020, 6, 6),
#     datetime(2020, 6, 7)
    
# ]

# y = [0,1,3,4,6,5,7]

# plt.plot_date(dates, y, linestyle='solid')



# plt.gcf().autofmt_xdate()

# date_format = mpl_dates.DateFormatter('%b, %d %Y')

# plt.gca().xaxis.set_major_formatter(date_format)

data = pd.read_csv('data5.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

# plt.legend()

# plt.title('Trending TouTube Videos')
# plt.xlabel('View Count')
# plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()

