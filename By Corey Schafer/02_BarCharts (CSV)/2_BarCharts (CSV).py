from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd
import numpy as np

plt.style.use('fivethirtyeight')

df = pd.read_csv('bar_data.csv')

print(df.head())

#most popular programming languages using barcharts

# c = Counter(['aa', 'aa', 'bb'])
# print(c)
#
# c.update(['aa', 'cc', 'dd'])
# print(c)

language_counter = Counter()

for language in df['LanguagesWorkedWith']:
    language_counter.update(language.split(';'))

print(language_counter)
print(language_counter.most_common(15)) #return list with tuple

x_language = []
y_popularity = []

for item in language_counter.most_common(15):
    x_language.append(item[0])
    y_popularity.append(item[1])

print(x_language)
print(y_popularity)

x_language.reverse()
y_popularity.reverse()

plt.barh(x_language, y_popularity)

plt.title('Most Popular Languages')
plt.xlabel('Number of People who use it')

plt.tight_layout()
plt.savefig('2_BarCharts (CSV).png')
plt.show()



