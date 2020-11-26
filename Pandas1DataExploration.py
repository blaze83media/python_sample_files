import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df=pd.read_csv('Pandas1Cleaned.csv') 

#Data Exploration
print(df.columns) 
print(df.head())

a1=df['PID']
a2=df['ST_NUM']
a3=df['ST_NAME']
a4=df['OWN_OCCUPIED']
a5=df['NUM_BEDROOMS']
a6=df['NUM_BATH']
a7=df['SQ_FT']

q1=[a2,a5,a6,a7]
colName=['ST_NUM','NUM_BEDROOMS','NUM_BATH','SQ_FT']
plt.boxplot(q1, notch=True, labels=colName)
plt.xlabel("Column")
plt.ylabel("value")
plt.title("Box Plot for Properties")
plt.legend
plt.show()


##plot #########
'''
sbt=plt.subplots()
br1=sbt.bar(a6)
br2=sbt.bar(a7)

plt.xlabel("Property details")
plt.ylabel("value")
plt.title("New Graph")
plt.legend
plt.show()
'''

#########################################################################

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()


#########################################################################
#single bar chart

N=9
ndx=np.arange(N)
width=0.30

a3N=df['ST_NAME']
a5c=df['NUM_BEDROOMS']
a6c=df['NUM_BATH']

a5SD=df['NUM_BEDROOMS'].describe()[2]
a6SD=df['NUM_BATH'].describe()[2]

pp1=plt.bar(ndx,a5c,width,yerr=a5SD)
pp2=plt.bar(ndx,a6c,width,yerr=a6SD,bottom=a5c)

plt.ylabel('Quantity')
plt.title('Property details')
plt.xticks(ndx, (a3N), rotation=50 )
plt.yticks(np.arange(0,6,1))
plt.legend((pp1[0], pp2[0]), ('Bathroom(s)', 'Room Size(sqr ft)'))

plt.show()


#########################################################################
#multi bar chart

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


############################################################################

#pie chart
'''
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()

'''

