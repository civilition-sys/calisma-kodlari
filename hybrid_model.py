import numpy as np

gamma11 = np.array([14.1347251417,21.0220396388,25.0108575801,30.4248761259,32.9350615877,37.5861781588,40.9187190122,43.3270732809,48.0051508812,49.7738324777,52.9703214777])

def rvm(n): return n*np.log(n)-n+np.log(2*np.pi)/2
asy = rvm(np.arange(1,12))
poly5 = np.polyfit(np.arange(1,12), gamma11-asy, 5)

def predict(n):
    return 0.62*rvm(n) + 0.27*np.polyval(poly5,n) + 0.11*0.0008*n

print("n=100000000 → γ ≈", predict(100000000))