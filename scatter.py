import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# x = [5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
# y = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]

# colors = [7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]

# plt.scatter(x,y, s=100, c=colors, cmap='Greens', edgecolors='black', linewidths=1, alpha=0.75)






data = pd.read_csv('data4.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']


plt.scatter(view_count,likes, c=ratio, cmap='summer',
            edgecolors='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike ratio')

plt.xscale('log')
plt.yscale('log')


plt.legend()

plt.title('Trending TouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()

