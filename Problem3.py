import numpy as np

def LinReg(a):
    if len(a) <= 10:
        al = len(a)
    else:
        al = 10
    
    for b in range(al):
        L = np.polyfit(a[:, 0], a[:, 1], b)
        e = np.linalg.norm(a[:, 1] - np.polyval(L, a[:, 0]))
        x = [b, e]
        if b == 0:
            y = x
        if y[1] >= x[1]:
            z = x[0]
            
    L = np.polyfit(a[:, 0], a[:, 1], z)
    
    return L