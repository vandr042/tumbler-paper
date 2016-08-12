import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def put(xvals, vp):
    for i in range(len(xvals)):
        if (vp <= xvals[i]):
            xvals.insert(i, vp)
            return i
    xvals.insert(len(xvals),vp)
    return len(xvals)
    

def FPvsVP(filename):
    f = open(filename, 'r')

    curFig = plt.figure()
    headers = f.readline()
    xvals = [0]
    yvals = [0.0]
    
    for line in f:
        arr = line.split(',')
        i = put(xvals,int(arr[0]))
        yvals.insert(i,float(arr[1]))
        
    plt.plot(xvals,yvals, label="c1", lw = 5.0, figure=curFig)

    #plt.legend(bbox_to_anchor=(0.,1.02,1.,.102), loc=2, ncol=5, mode = "expand", borderaxespad=0)
    plt.xlabel("Vantage Points")
    plt.ylabel("First Peer ID Accuracy")
    curFig.savefig("../plots/FPvsVP.pdf", format="pdf")
    
def ASvsVPvsCS(filename):
    f = open(filename, 'r')

    headers = f.readline()

    xvals = [0]
    c25yvals = [0.0]
    c10yvals = [0.0]
    c5yvals = [0.0]
    c4yvals = [0.0]
    c2yvals = [0.0]
    c1yvals = [0.0]
    
    for line in f:
        arr = line.split(',')
        i = put(xvals,int(arr[0]))
        c25yvals.insert(i,float(arr[12]))
        c10yvals.insert(i,float(arr[10]))
        c5yvals.insert(i,float(arr[8]))
        c4yvals.insert(i,float(arr[6]))
        c2yvals.insert(i,float(arr[4]))
        c1yvals.insert(i,float(arr[2]))

    curFig = plt.figure()
    plt.plot(xvals,c1yvals, label = "c1", figure=curFig, lw = 5.0)
    plt.plot(xvals,c2yvals, label = "c2", figure=curFig, lw = 5.0)
    plt.plot(xvals,c4yvals, label = "c4", figure=curFig, lw = 5.0)
    plt.plot(xvals,c5yvals, label = "c5", figure=curFig, lw = 5.0)
    plt.plot(xvals,c10yvals, label = "c10", figure=curFig, lw = 5.0)
    plt.plot(xvals,c25yvals, label = "c25", figure=curFig, lw = 5.0)
    
    plt.legend(bbox_to_anchor=(0.,1.02,1.,.102), loc=2, ncol=5, mode = "expand", borderaxespad=0)
    plt.xlabel("Vantage Points")
    plt.ylabel("Anonymity Set Size")
    plt.yscale('log')
    curFig.savefig("../plots/ASvsVPvsCS.pdf", format="pdf")
    
def TPvsVPvsCS(filename):
    f = open(filename, 'r')

    headers = f.readline()
    xvals = [0]
    c25yvals = [0.0]
    c10yvals = [0.0]
    c5yvals = [0.0]
    c4yvals = [0.0]
    c2yvals = [0.0]
    c1yvals = [0.0]

    curFig = plt.figure()
    for line in f:
        arr = line.split(',')
        i = put(xvals,int(arr[0]))
        c25yvals.insert(i,float(arr[13]))
        c10yvals.insert(i,float(arr[11]))
        c5yvals.insert(i,float(arr[9]))
        c4yvals.insert(i,float(arr[7]))
        c2yvals.insert(i,float(arr[5]))
        c1yvals.insert(i,float(arr[3]))
        
    plt.plot(xvals,c1yvals, label = "c1", figure=curFig, lw = 5.0)
    plt.plot(xvals,c2yvals, label = "c2", figure=curFig, lw = 5.0)
    plt.plot(xvals,c4yvals, label = "c4", figure=curFig, lw = 5.0)
    plt.plot(xvals,c5yvals, label = "c5", figure=curFig, lw = 5.0)
    plt.plot(xvals,c10yvals, label = "c10", figure=curFig, lw = 5.0)
    plt.plot(xvals,c25yvals, label = "c25", figure=curFig, lw = 5.0)

    plt.legend(bbox_to_anchor=(0.,1.02,1.,.102), loc=2, ncol=5, mode = "expand", borderaxespad=0)
    plt.xlabel("Vantage Points")
    plt.ylabel("True Positive Rate")
    curFig.savefig("../plots/TPvsVPvsCS.pdf", format="pdf")

