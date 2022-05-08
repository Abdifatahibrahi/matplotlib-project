import csv
import numpy as np
from cProfile import label
from turtle import color
from matplotlib import pyplot as plt
from collections import Counter


# print(plt.style.available)

plt.style.use('ggplot')


with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(tuple(zip(languages, popularity)))

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)


plt.ylabel('Programming languages')
plt.xlabel('Number of people who use')

plt.title('Most popular languages')

plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.grid(True)
plt.tight_layout()

# plt.savefig('plot.png')

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

