import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta


plt.style.use('seaborn')

# x = [5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
# y = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]

# colors = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]

# plt.scatter(x,y, s=100, c=colors, cmap='Greens', edgecolors='black', linewidths=1, alpha=0.75)


dates = [
    datetime(2020, 6, 1),
    datetime(2020, 6, 2),
    datetime(2020, 6, 3),
    datetime(2020, 6, 4),
    datetime(2020, 6, 5),
    datetime(2020, 6, 6),
    datetime(2020, 6, 7)
    
]

y = [0,1,3,4,6,5,7]

plt.plot_date(dates, y, linestyle='solid')



plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b, %d %Y')

plt.gca().xaxis.set_major_formatter(date_format)

# data = pd.read_csv('data4.csv')
# view_count = data['view_count']
# likes = data['likes']
# ratio = data['ratio']


# plt.legend()

# plt.title('Trending TouTube Videos')
# plt.xlabel('View Count')
# plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()

