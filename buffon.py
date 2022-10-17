import random
import matplotlib.pyplot as plt
import math
import numpy as np

width = 50
length = 40

def monte_carlo(n):
    pi_line = [math.pi]*n
    hit = 0
    prob_list = []
    for i in range(n):
        distance_from = random.uniform(0,width)
        angle = random.uniform(0,math.pi/2)
        if distance_from + (length*math.cos(angle)) > width:
            hit += 1
        prob_list.append(hit/(i+1))
    print(((hit/n)*width)**-1 * (2*length))
    pi_list = ((np.array(prob_list) * width)**-1)*(2*length)
    plt.xlabel("number of iterations")
    plt.ylabel("extracted value of pi")
    plt.title("Buffon's Needle Monte Carlo simulation")
    plt.plot(pi_list, label="extracted pi value")
    plt.plot(pi_line, label="pi")
    plt.show()

monte_carlo(20000)
    

    
    

        

    