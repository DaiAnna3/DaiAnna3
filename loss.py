import matplotlib.pyplot as plt
import pandas as pd

# 读取Excel文件中的数据，假设文件名为loss.xlsx，第一列是g_loss，第二列是d_loss
data = pd.read_excel('loss.xlsx')

# 获取g_loss和d_loss列的数据，这里假设数据没有表头，如果有表头请根据实际情况调整
g_loss = data.iloc[:, 0].tolist()
d_loss = data.iloc[:, 1].tolist()

# 打印原始g_loss和d_loss的长度（形状）
print("原始g_loss的长度（形状）:", len(g_loss))
print("原始d_loss的长度（形状）:", len(d_loss))

# 生成从0到299的整数序列作为横坐标x的值，对应300次迭代，步长为1
x = range(300)

# 每隔3个取一个数据点，确保g_loss和d_loss长度与x一致
new_g_loss = g_loss[::4]
new_d_loss = d_loss[::4]

# 打印处理后new_g_loss和new_d_loss的长度（形状）
print("处理后new_g_loss的长度（形状）:", len(new_g_loss))
print("处理后new_d_loss的长度（形状）:", len(new_d_loss))

# 绘制折线图
plt.plot(x, new_g_loss, label='g_loss', marker='o')
plt.plot(x, new_d_loss, label='d_loss', marker='s')

# 添加图表的标题和坐标轴标签
plt.title('Loss Variation during 300 Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')

# 添加图例
plt.legend()

# 显示网格，使图表更清晰
plt.grid(True)

# 显示图形
plt.show()