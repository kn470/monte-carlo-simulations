import matplotlib.pyplot as plt
import numpy as np
import random
import threading

def flip():
    return random.randint(0,1)

def monte_carlo(n):
    prob_list = []
    cumulative_result = 0
    for i in range(n):
        coin_toss = flip()
        cumulative_result += coin_toss
        prob_val = cumulative_result/(i+1)
        prob_list.append(prob_val)

    print(cumulative_result/n)
    plt.title("Coin Flip Monte Carlo Simulation")
    plt.xlabel("Iteration number")
    plt.ylabel("Average cumulative probability of a heads")
    plt.plot(prob_list)
    plt.show()

    


monte_carlo(5000)

