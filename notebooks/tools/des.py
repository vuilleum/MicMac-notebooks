

import numpy as np
import scipy.optimize as opt

def OneStep(des,ndes,nfaces):
    i=np.random.randint(0,ndes)
    j=i
    while (j==i):
        j=np.random.randint(0,ndes)

    destrial=np.copy(des)
    destrial[i]-=1
    destrial[j]+=1

    if (destrial[i]>0) and (destrial[j]<nfaces+1):
        return destrial
    else:
        return np.copy(des)

def DicesToString(des):
    destexte=""
    for i in range(len(des)-1):
        destexte+=str(des[i])+"-"
    destexte+=str(des[-1])

    return destexte

def StringToDice(destexte):
    liste=destexte.split('-')
    des=np.zeros(len(liste))
    for i,s in enumerate(liste):
        des[i]=np.int(s)
    return des

def TiragesDes(ndes=3,somme=8,nfaces=6,ntirages=100,npas=10):
    tirages=np.zeros((ndes,ntirages),dtype=np.int)

    if ((somme<ndes) or (somme>nfaces*ndes)):
        raise ValueError("La valeur de l'argument somme n'est pas valide" )

    desinit=np.ones(ndes)*somme//ndes
    desinit[0:somme%ndes]=desinit[0:somme%ndes]+1

    des=np.copy(desinit)
    for tirage in range(ntirages):
        for pas in range(npas):
            des=OneStep(des,ndes,nfaces)
        tirages[:,tirage]=np.copy(des)

    return tirages

def HistogrammeDes(tirages):
    ndes,ntirages=tirages.shape
    hist={}
    for i in range(ntirages):
        des=tirages[:,i]
        txt=DicesToString(des)
        hist[txt]=hist.get(txt,0)+1

    return hist

def Proba(tirages,ides,nfaces=6):
    ndes,ntirages=tirages.shape
    if (ides>ndes):
        raise ValueError("Le numéro du dé demandé, {}, est plus grand que le nombre de dés utilisé pour générer tirages, {}".format(ides,ndes))
        
    proba=np.zeros(nfaces)
    for i in range(nfaces):
        proba[i]=np.sum(tirages[ides,:]==i+1)/ntirages

    return proba

def f(x,nfaces,target):
    mean=(nfaces*x**(nfaces+1)-(nfaces+1)*x**nfaces+1)/(x**(nfaces+1)-x**nfaces-x+1)
    return mean-target

def BoltzmannParam(mean,nfaces=6):
    sol=opt.root_scalar(f,args=(nfaces,mean),x0=0.3,x1=0)
    x=sol.root
    n0=-1/np.log(x)
    q=(x**nfaces-1)/(x-1)*x

    return n0,q
