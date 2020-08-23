from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

df = pd.read_csv('histogram_data.csv')
print(df.head())

ids = df['Responder_id']
ages = df['Age']
avg_age = 29

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #10-20 in a bin, 20-30 in another bin and so on...

# ag = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
# plt.hist(ag, bins = bins, edgecolor = 'black')

plt.hist(ages, bins = bins, edgecolor = 'black', log = True) #show data in logarithmic scale
plt.axvline(avg_age, color = '#fc4f30', label = 'Age Median', linewidth = 2) #axis vertical line

plt.title('Histograms')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.legend()
plt.tight_layout()
plt.savefig('6_Histogram.png')
plt.show()