
import numpy as np

def pileface():
    cote=np.random.randint(0,2)
    switcher={0: "Pile", 1: "Face"}
    return switcher[cote]

def zeroun():
    return np.random.randint(0,2)
