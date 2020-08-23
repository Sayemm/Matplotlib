from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Fourty', 'Extra1', 'Extra2']
# colors = ['#008fd5', 'red', 'yellow', 'green']
#
# plt.pie(slices, labels=labels, colors = colors, wedgeprops={'edgecolor': 'black'})

#Pychart is better for less items <= 5/6

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0] #how much away from radius 0.1 = 10%

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, explode = explode, shadow=True, startangle=90, autopct='%1.1f%%')

plt.title('Pie Chart')
plt.tight_layout()
plt.savefig('3_PieCharts.png')
plt.show()