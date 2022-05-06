from cProfile import label
from turtle import color
from matplotlib import pyplot as plt


# print(plt.style.available)

plt.style.use('ggplot')


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 68748, 73752]

plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370]

plt.plot(ages_x, py_dev_y, label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746]

plt.plot(ages_x, js_dev_y, label='Javascript')


plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')

plt.title('Median Salary (USD) by Age')

plt.legend()

# plt.grid(True)
plt.tight_layout()

plt.savefig('plot.png')

plt.show()



# ['Solarize_Light2', '_classic_test_patch', 
# '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 
# 'classic', 'dark_background', 'fast', 'fivethirtyeight', 
# 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright',
#  'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 
# 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
# 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 
# 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 
# 'seaborn-whitegrid', 'tableau-colorblind10']