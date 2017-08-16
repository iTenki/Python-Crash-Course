import matplotlib.pyplot as plt

x_value = list(range(1, 1000))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, s = 100 )

# 设置图标标题 并给坐标轴加上标签
plt.title("Square Number", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params([0, 1100, 0, 1100000])

plt.show()