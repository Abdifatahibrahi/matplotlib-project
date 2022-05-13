from cProfile import label
from tkinter import TRUE
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]



data = pd.read_csv("data3.csv")
ids = data['Responder_id']
ages = data['Age']

plt.hist(ages, bins=bins, edgecolor='black', log=True)




plt.legend()

plt.title('Ages of respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()

