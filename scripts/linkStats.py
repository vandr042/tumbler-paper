import numpy as np
import matplotlib.pyplot as plt

def FPvsVP(filename):
    f = open(filename, 'r')

    headers = f.readline()
    xvals = [0]
    yvals = [0.0]
    
    for line in f:
        arr = line.split(',')
        xvals.append(int(arr[0]))
        yvals.append(float(arr[1]))
        
    plt.plot(xvals,yvals)

    plt.xlabel("Vantage Points")
    plt.ylabel("First Peer ID Accuracy")
    plt.show()

def ASvsVPvsCS(filename):
    f = open(filename, 'r')

    headers = f.readline()
    xvals = [0]
    c10yvals = [0.0]
    c5yvals = [0.0]
    c4yvals = [0.0]
    c2yvals = [0.0]
    c1yvals = [0.0]
    
    for line in f:
        arr = line.split(',')
        xvals.append(int(arr[0]))
        c10yvals.append(float(arr[10]))
        c5yvals.append(float(arr[8]))
        c4yvals.append(float(arr[6]))
        c2yvals.append(float(arr[4]))
        c1yvals.append(float(arr[2]))
        
    plt.plot(xvals,c10yvals)
    plt.plot(xvals,c5yvals)
    plt.plot(xvals,c4yvals)
    plt.plot(xvals,c2yvals)
    plt.plot(xvals,c1yvals)

    plt.xlabel("Vantage Points")
    plt.ylabel("Anonymity Set Size")
    plt.show()

def TPvsVPvsCS(filename):
    f = open(filename, 'r')

    headers = f.readline()
    xvals = [0]
    c10yvals = [0.0]
    c5yvals = [0.0]
    c4yvals = [0.0]
    c2yvals = [0.0]
    c1yvals = [0.0]
    
    for line in f:
        arr = line.split(',')
        xvals.append(int(arr[0]))
        c10yvals.append(float(arr[11]))
        c5yvals.append(float(arr[9]))
        c4yvals.append(float(arr[7]))
        c2yvals.append(float(arr[5]))
        c1yvals.append(float(arr[3]))
        
    plt.plot(xvals,c10yvals)
    plt.plot(xvals,c5yvals)
    plt.plot(xvals,c4yvals)
    plt.plot(xvals,c2yvals)
    plt.plot(xvals,c1yvals)

    plt.xlabel("Vantage Points")
    plt.ylabel("True Positive Rate")
    plt.show()

