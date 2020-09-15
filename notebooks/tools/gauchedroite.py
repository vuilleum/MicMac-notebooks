
import numpy as np

def nouveautirage(Nparticules=10,Verbose=False):
    tirage=np.random.randint(0,2,Nparticules)
    result={"Gauche": np.sum(tirage==0), "Droite": np.sum(tirage==1)}

    if Nparticules>100:
        Verbose=False
    if (Verbose):
        switcher={0:"Gauche", 1:"Droite"}
        return ([switcher.get(tirage[i]) for i in range(Nparticules)],result)
    else:
        return result
