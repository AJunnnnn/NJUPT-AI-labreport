import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# 生成不同类型的网络
def generate_networks(num_nodes, prob, k, p, m):
    ER_net = nx.erdos_renyi_graph(num_nodes, prob)
    WS_net = nx.watts_strogatz_graph(num_nodes, k, p)
    BA_net = nx.barabasi_albert_graph(num_nodes, m)
    return ER_net, WS_net, BA_net


# 加载真实网络
def load_real_network():
    real_net = nx.karate_club_graph()  # 这里以Karate Club网络为例
    return real_net


# SIR模型的蒙特卡洛模拟
def sir_model(G, beta, gamma, initial_infected, max_time):
    S = np.ones(G.number_of_nodes())
    I = np.zeros(G.number_of_nodes())
    R = np.zeros(G.number_of_nodes())

    I[initial_infected] = 1
    S[initial_infected] = 0

    S_t = [np.sum(S)]
    I_t = [np.sum(I)]
    R_t = [np.sum(R)]

    for t in range(max_time):
        new_I = []
        new_R = []

        for i in range(len(I)):
            if I[i] == 1:
                neighbors = list(G.neighbors(i))
                for neighbor in neighbors:
                    if S[neighbor] == 1 and np.random.rand() < beta:
                        new_I.append(neighbor)
                if np.random.rand() < gamma:
                    new_R.append(i)

        for i in new_I:
            S[i] = 0
            I[i] = 1
        for i in new_R:
            I[i] = 0
            R[i] = 1

        S_t.append(np.sum(S))
        I_t.append(np.sum(I))
        R_t.append(np.sum(R))

    return S_t, I_t, R_t


# 运行多次模拟以获得平滑的曲线
def run_simulation(G, beta, gamma, initial_infected, max_time, num_simulations):
    avg_I_t = np.zeros(max_time + 1)

    for _ in range(num_simulations):
        _, I_t, _ = sir_model(G, beta, gamma, initial_infected, max_time)
        avg_I_t += I_t

    avg_I_t /= num_simulations
    return avg_I_t


# 参数设置
num_nodes = 1000
prob = 0.1
k = 4
p = 0.1
m = 3

beta = 0.3
gamma = 0.1
initial_infected = [0]
max_time = 100
num_simulations = 50

# 生成网络
ER_net, WS_net, BA_net = generate_networks(num_nodes, prob, k, p, m)
real_net = load_real_network()

# 运行时间演化模拟
avg_I_t_ER = run_simulation(ER_net, beta, gamma, initial_infected, max_time, num_simulations)
avg_I_t_WS = run_simulation(WS_net, beta, gamma, initial_infected, max_time, num_simulations)
avg_I_t_BA = run_simulation(BA_net, beta, gamma, initial_infected, max_time, num_simulations)
avg_I_t_real = run_simulation(real_net, beta, gamma, initial_infected, max_time, num_simulations)

# 绘制时间演化曲线
plt.figure(figsize=(10, 6))
plt.plot(avg_I_t_ER, label="ER Network")
plt.plot(avg_I_t_WS, label="WS Network")
plt.plot(avg_I_t_BA, label="BA Network")
plt.plot(avg_I_t_real, label="Real Network (Karate Club)")
plt.xlabel("Time")
plt.ylabel("Infected Individuals")
plt.title("Time Evolution of Infection in SIR Model")
plt.legend()
plt.show()
