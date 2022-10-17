import random
import matplotlib.pyplot as plt
import math



def monte_carlo(n):
    line1 = [(1/3)]*math.floor(n*(2/3))
    line2 = [(2/3)]*math.floor(n*(2/3))
    doors = ["goat", "goat", "car"]
    stick_win_prob = []
    switch_win_prob = []
    stick_win = 0
    switch_win = 0
    for i in range(n):
        random.shuffle(doors)
        pick = random.randint(0,2)
        if doors[pick] == "car":
            stick_win += 1
            stick_win_prob.append(stick_win/(i+1))
        else:
            switch_win += 1
            switch_win_prob.append(switch_win/(i+1))

    print("stick win:", stick_win, "switch win:", switch_win)
    plt.xlabel("number of trials")
    plt.ylabel("probability of success")
    plt.title("Monty Hall Monte Carlo simulation")
    plt.plot(stick_win_prob, label="stick")
    plt.plot(switch_win_prob, label="switch")
    plt.plot(line1, label="p=1/3")
    plt.plot(line2, label="p=2/3")
    plt.legend()
    plt.show()

monte_carlo(20000)
