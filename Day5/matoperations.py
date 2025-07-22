import matplotlib.pyplot as plt

#basic line plot
x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y)
plt.title("line chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()

#barchart
categories=['A','B','C']
values=[10,20,15]

plt.bar(categories,values)
plt.title("bargraph")
plt.show()

#scatter plot
x=[1,2,3,4,5]
y=[2,4,1,8,7]
plt.scatter(x,y, color='blue')
plt.title("scatter plot")
plt.xlabel("X")
plt.show()
