from matplotlib import dates
import pandas as pd  
import matplotlib.pyplot as plt  

plt.rcParams['font.size'] = 20  # 设置全局字体大小为14

  
# 假设df是一个包含日期、收盘价和涨跌幅（百分比形式）的DataFrame  
# df['涨跌幅'] = ... # 涨跌幅数据，假设已经是小数形式，例如5%为0.05  
# 读取Excel文件  
df = pd.read_excel('上证指数.xlsx')  
  
# 确保'日期'列是日期格式  
df['日期'] = pd.to_datetime(df['日期'])  
df['日期'] = df['日期'].dt.date 

  
# 设置Matplotlib字体为宋体（或其他支持中文的字体）  
plt.rcParams['font.sans-serif'] = ['SimSun']  # 指定默认字体为宋体  
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号显示为方块的问题  
  
# 绘制图表  
fig, ax1 = plt.subplots(figsize=(16, 10))  
  
# 原始轴（左侧）用于收盘价  
ax1.plot(df['日期'], df['收盘'], label='收盘价', color='black')  
ax1.set_xlabel('日期')  
ax1.set_ylabel('收盘价', color='black')  
ax1.set_ylim(2000, 4000)  # 设置y轴范围  
ax1.tick_params('y', colors='black')  # 设置y轴刻度颜色  

# 设置日期格式  
date_format = dates.DateFormatter('%Y/%m/%d')  
ax1.xaxis.set_major_formatter(date_format)  
  
# 第二个轴（右侧）用于涨跌幅  
ax2 = ax1.twinx()  
  
# 自定义柱状图的颜色（绿色为跌幅，红色为涨幅）  
colors = ['red' if x > 0 else 'green' for x in df['涨跌幅']]  
bars = ax2.bar(df['日期'], df['涨跌幅'], label='涨跌幅', color=colors)  
  
# 设置y轴标签和范围  
ax2.set_ylabel('涨跌幅', color='black')  
ax2.set_ylim(-0.05, 0.05)  # 涨跌幅范围是-5%到5%  
  
# 自定义y轴刻度标签的颜色  
for tick, color in zip(ax2.get_yticklabels(), ['red' if y > 0 else 'green' for y in ax2.get_yticks()]):  
    tick.set_color(color)  

# 在特定日期位置画纵虚线  
date_to_mark = pd.to_datetime('2021/9/13')  
ax1.axvline(x=date_to_mark, color='gray', linestyle='--', label='特定日期')  
  
# 在纵虚线位置添加日期标签  
ax1.text(date_to_mark, ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * 0.02,   
         date_to_mark.strftime('%Y/%m/%d'), rotation=90, va='bottom', color='gray')

# 自定义图例句柄和标签  
handles, labels = ax2.get_legend_handles_labels()  
new_handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in ['green', 'red']]  
new_labels = ['跌幅', '涨幅']  
  
# 添加图例  
ax2.legend(new_handles, new_labels, loc='upper right')  
  
# 设置图表标题  
plt.title('上证指数收盘价与涨跌幅')  
  
# 旋转x轴标签以便阅读  
plt.xticks(rotation=45)  
  
# 显示图表  
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域  
plt.show()

# 保存图表为PDF格式  
plt.savefig('涨跌幅.pdf', format='pdf')
