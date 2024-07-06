# import networkx as nx
# import random
# import matplotlib.pyplot as plt
#
#
# def modified_ba_graph(n, m, p_triangle):
#     """
#     生成一个修改后的BA模型，考虑三角形闭合以提高聚类系数。
#     n: 节点总数
#     m: 每次添加节点时连接到已有网络中的边数
#     p_triangle: 形成三角形的概率
#     """
#     G = nx.complete_graph(m)
#
#     for i in range(m, n):
#         new_edges = set()
#         targets = set(random.sample(G.nodes(), m))
#         new_edges.update((i, t) for t in targets)
#
#         # 形成三角形的部分
#         for t in targets:
#             if random.random() < p_triangle:
#                 neighbors = set(G.neighbors(t))
#                 if neighbors:
#                     neighbor = random.choice(list(neighbors))
#                     new_edges.add((i, neighbor))
#
#         G.add_edges_from(new_edges)
#
#     return G
#
#
# # 生成修改后的BA模型
# G_modified = modified_ba_graph(10000, 3, 0.6)  # 将三角形闭合的概率提高到0.6
#
# # 获取统计特征
# degree_modified = dict(nx.degree(G_modified))
# average_degree_modified = sum(degree_modified.values()) / len(G_modified)
# average_shortest_path_length_modified = nx.average_shortest_path_length(G_modified)
# average_clustering_modified = nx.average_clustering(G_modified)
#
# # 打印统计特征
# print("修改后的BA模型统计特征：")
# print("平均度为：", average_degree_modified)
# print("最短路径长度为：", average_shortest_path_length_modified)
# print("平均聚类系数为：", average_clustering_modified)
#
# # 度分布图
# degree_distribution_modified = nx.degree_histogram(G_modified)
# x_modified = range(len(degree_distribution_modified))
# y_modified = [z / float(sum(degree_distribution_modified)) for z in degree_distribution_modified]
# plt.figure(figsize=(5.8, 5.2), dpi=150)
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.xlabel("Degree", size=14)  # Degree
# plt.ylabel("Frequency", size=14)  # Frequency
# plt.xticks(fontproperties='Times New Roman', size=13)  # 字体样式
# plt.yticks(fontproperties='Times New Roman', size=13)  # 字体样式
# plt.loglog(x_modified, y_modified, '.')  # 对数化坐标
# plt.show()

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def generate_random_geometric_graph(N, L, r):
    """
    生成随机几何图
    N: 节点总数
    L: 空间边长
    r: 连接半径
    """
    # 生成随机点
    points = np.random.rand(N, 2) * L

    # 创建图
    G = nx.Graph()

    # 添加节点
    for i, (x, y) in enumerate(points):
        G.add_node(i, pos=(x, y))

    # 添加边
    for i in range(N):
        for j in range(i + 1, N):
            dist = np.linalg.norm(points[i] - points[j])
            if dist <= r:
                G.add_edge(i, j)

    return G


# 参数设置
N = 1000  # 节点总数
L = 1.0  # 空间边长
r = 0.05  # 连接半径

# 生成随机几何图
G_rgg = generate_random_geometric_graph(N, L, r)

# 检查图的连通性，如果不连通则提取最大连通子图
if not nx.is_connected(G_rgg):
    largest_cc = max(nx.connected_components(G_rgg), key=len)
    G_rgg = G_rgg.subgraph(largest_cc).copy()

# 获取统计特征
degree_rgg = dict(nx.degree(G_rgg))
average_degree_rgg = sum(degree_rgg.values()) / len(G_rgg)
average_shortest_path_length_rgg = nx.average_shortest_path_length(G_rgg)
average_clustering_rgg = nx.average_clustering(G_rgg)

# 打印统计特征
print("随机几何图模型统计特征：")
print("平均度为：", average_degree_rgg)
print("最短路径长度为：", average_shortest_path_length_rgg)
print("平均聚类系数为：", average_clustering_rgg)

# 绘制图
pos = nx.get_node_attributes(G_rgg, 'pos')
nx.draw(G_rgg, pos, node_size=30, with_labels=False)
plt.show()

# 度分布图
degree_distribution_rgg = nx.degree_histogram(G_rgg)
x_rgg = range(len(degree_distribution_rgg))
y_rgg = [z / float(sum(degree_distribution_rgg)) for z in degree_distribution_rgg]
plt.figure(figsize=(5.8, 5.2), dpi=150)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.xlabel("Degree", size=14)  # Degree
plt.ylabel("Frequency", size=14)  # Frequency
plt.xticks(fontproperties='Times New Roman', size=13)  # 字体样式
plt.yticks(fontproperties='Times New Roman', size=13)  # 字体样式
plt.loglog(x_rgg, y_rgg, '.')  # 对数化坐标
plt.show()
