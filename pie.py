from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [120, 80, 30, 20]
labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
colors = ['blue', 'red', 'yellow', 'green']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()