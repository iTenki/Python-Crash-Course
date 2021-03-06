import matplotlib.pyplot as plt

x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
plt.scatter(x_value, y_value,c = y_value, cmap=plt.cm.Blues, edgecolor = 'none', s = 100 )

# 设置图标标题 并给坐标轴加上标签
plt.title("Square Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()