import numpy as np
import random
import matplotlib.pyplot as plt
import math

#we will generate a 500 by 500 square, with a circle of radius 250

#here we will generate a point in this square
def generate_point():
    x = random.randint(0,500)
    y = random.randint(0,500)
    return [x,y]

#here we will write a function to determine whether it lies in the circle or not
def in_circle(point):
    if ((point[0]-250)**2 + (point[1]-250)**2)**0.5 < 250:
        return True
    else:
        return False

def simulate(n):
    generate_count = 1
    circle_count = 0
    for i in range(n):
        point = generate_point()
        generate_count += 1
        inside = in_circle(point)
        if inside:
            circle_count += 1

    circle_square_ratio = circle_count/generate_count
    return circle_square_ratio*4

def plot(n):
    prob_list = []
    cumulative_result = 0
    for i in range(n):
        cumulative_result += simulate(i)
        prob_val = cumulative_result/(i+1)
        prob_list.append(prob_val)

    print(cumulative_result/n)
    plt.xlabel("Number of Iterations")
    plt.ylabel("Extracted value of pi")
    plt.plot(prob_list)
    line = [math.pi]*len(prob_list)
    plt.plot(line)
    plt.show()

plot(4000)


