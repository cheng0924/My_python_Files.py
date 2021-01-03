import pandas as pd
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

data = pd.DataFrame(pd.read_excel('E:\\Python\\project-1\\数据挖掘\\4-13.xlsx'))
user_id = data['用户昵称']
data = data.loc[:, ['粉丝数', '关注数', '微博数', '收藏数', '互粉数']]
data1 = pd.concat([user_id, data], axis=1)
data_zs = (data-data.mean())/data.std()

label=data.columns.values

model = KMeans(n_clusters=4)
model.fit(data)

r = pd.concat([data1, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data1.columns)+[u'聚类类别']
r.to_excel("聚类结果.xls")


tsne = TSNE()
tsne.fit_transform(data_zs)  # 进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index)  # 转换数据格式


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.', label='0')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go', label='1')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*', label='2')
d = tsne[r[u'聚类类别'] == 3]
plt.plot(d[0], d[1], 'ko', label='3')
plt.legend(loc='upper right')
plt.show()
