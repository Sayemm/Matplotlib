from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

df = pd.read_csv('fill_data.csv')
print(df.head())

ages = df['Age']
dev_salaries = df['All_Devs']
py_salaries = df['Python']
js_salaries = df['JavaScript']

avg_salary = 57287

plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')
plt.plot(ages, py_salaries, label = 'Python')

# plt.fill_between(ages, py_salaries, y2 = avg_salary, alpha = 0.25, where=(py_salaries > avg_salary), interpolate=True) #alpha = density
# plt.fill_between(ages, py_salaries, y2 = avg_salary, alpha = 0.25, where=(py_salaries <= avg_salary), interpolate=True, color = 'red')

plt.fill_between(ages, py_salaries, y2 = dev_salaries, alpha = 0.25, where=(py_salaries > dev_salaries), interpolate=True, label = 'Above Avg') #alpha = density
plt.fill_between(ages, py_salaries, y2 = dev_salaries, alpha = 0.25, where=(py_salaries <= dev_salaries), interpolate=True, color = 'red', label = 'Below Avg')

plt.title('Fill Area')
plt.xlabel('Ages')
plt.ylabel('Salary')

plt.legend()
plt.tight_layout()

plt.savefig('5_FillArea.png')
plt.show()