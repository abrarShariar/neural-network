import math
import random

def getInput():
    i1 = random.uniform(0.01, 1.00)
    i2 = random.uniform(0.01, 1.00)
    return i1, i2

def calculateTotalError():
    # target
    to1, to2 = 0.01, .99
    
    # input
    i1, i2 = getInput()

    # weights
    w1, w2, w3, w4, w5, w6, w7, w8 = .15, .20, .25, .30, .40, .45, .50, .55

    # bias
    b1, b2 = 1, 1
    b1w, b2w = .35, .60

    # calculate the net input of h1
    neth1 = (w1 * i1) + (w2 * i2) + (b1 * b1w)
    #print("neth1=", neth1)

    outh1 = 1 /(1 + math.exp(-neth1))
    #print("outh1=", outh1)

    # calculate the net output for h2
    neth2 = (w3 * i1) + (w4 * i2) + (b1 * b1w)
    #print("neth2=", neth2)

    outh2 = 1 / (1 + math.exp(-neth2))
    #print("outh2=", outh2)

    #calculate net output of o1
    neto1 = (w5 * outh1) + (w6 * outh2) + (b2 * b2w)
    #print("neto1=", neto1)

    outo1 = 1 / (1 + math.exp(-neto1))
    #print("outo1=", outo1)

    # calculate output for o2
    neto2 = (w7 * outh1) + (w8 * outh2) + (b2 * b2w)
    #print("neto2=", neto2)

    outo2 = 1 / (1 + math.exp(-neto2))
    #print("outo2=", outo2)

    # calculating total error E_o1
    E_o1 = 0.5 * (to1 - outo1)**2
    #print("E_o1=", E_o1)

    # calculating total error for E_o2
    E_o2 = 0.5 * (to2 - outo2)**2
    #print("E_o2=", E_o2)

    # total error
    E_total = E_o1 + E_o2
    print("Total ERROR=", E_total)
    # print("\n")

for i in range(100):
    calculateTotalError()
