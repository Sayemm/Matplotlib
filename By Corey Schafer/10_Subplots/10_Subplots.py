import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

df = pd.read_csv('subplot_data.csv')
print(df.head())

ages = df['Age']
dev_salaries = df['All_Devs']
py_salaries = df['Python']
js_salaries = df['JavaScript']

# fig, ax = plt.subplots()
#
# ax.plot(ages, py_salaries, label = 'Python')
# ax.plot(ages, js_salaries, label = 'JavaScript')
# ax.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')
#
# ax.legend()
#
# ax.set_title('Median Salary')
# ax.set_xlabel('Ages')
# ax.set_ylabel('Salary')
#
# plt.tight_layout()
# plt.show()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True) #same figure
# fig1, ax1 = plt.subplots() #different figure
# fig2, ax2 = plt.subplots()

print(ax1)
print(ax2)

ax1.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')
ax2.plot(ages, py_salaries, label = 'Python')
ax2.plot(ages, js_salaries, label = 'JavaScript')

ax1.legend()
ax1.set_title('Median Salary')
ax1.set_ylabel('Salary')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Salary')

plt.tight_layout()
plt.show()

# fig1.savefig('10_Subplots1.png')
# fig2.savefig('10_Subplots2.png')

fig.savefig('10_Subplots.png')