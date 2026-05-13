import matplotlib.pyplot as plt

numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['red', 'green', 'pink', 'yellow']
explodelist = [0.1, 0.0, 0.0, 0.0]

plt.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist, explode=explodelist, startangle=90)
plt.axis('equal')
plt.savefig('piechart.png')
