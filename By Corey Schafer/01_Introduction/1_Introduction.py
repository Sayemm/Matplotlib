from matplotlib import pyplot as plt

# print(plt.style.available)
plt.style.use('ggplot')
# plt.xkcd() #xkcd comics

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, dev_y, 'k+--', label = 'All devs') #Format String [Color][Marker][Line]
plt.plot(ages_x, py_dev_y, color = 'b', marker = '*', linestyle = ':', label = 'Python devs', linewidth = 3) #color = '#444444' --> Hex value (rgb*2)
plt.plot(ages_x, js_dev_y, color = '#adad3b', label = 'JavaScript', linewidth = 3)

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

# plt.legend(['All devs', 'Python devs'])
plt.legend()

plt.grid(True)

plt.tight_layout() #Better Padding

plt.savefig('1_Introduction.png')

plt.show()