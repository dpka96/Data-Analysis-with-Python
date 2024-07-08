import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    
    a=np.array(list).reshape(3,3)
    #mean, variance, standard deviation, max, min, and sum
    rm=a.mean(axis=0)
    rv=a.var(axis=0)
    rstd=a.std(axis=0)
    rmax=a.max(axis=0)
    rmin=a.min(axis=0)
    rsum=a.sum(axis=0)

    cm=a.mean(axis=1)
    cv=a.var(axis=1)
    cstd=a.std(axis=1)
    cmax=a.max(axis=1)
    cmin=a.min(axis=1)
    csum=a.sum(axis=1)

    fm=a.mean()
    fv=a.var()
    fstd=a.std()
    fmax=a.max()
    fmin=a.min()
    fsum=a.sum()
 #mean, variance, standard deviation, max, min, and sum
    mean=[rm.tolist(),cm.tolist(),fm.tolist()]
    variance=[rv.tolist(),cv.tolist(),fv.tolist()]
    standarddev=[rstd.tolist(),cstd.tolist(),fstd.tolist()]
    maxx=[rmax.tolist(),cmax.tolist(),fmax.tolist()]
    minn=[rmin.tolist(),cmin.tolist(),fmin.tolist()]
    summ=[rsum.tolist(),csum.tolist(),fsum.tolist()]

    calculations = {
        "mean" : mean, 
        "variance" : variance, 
        "standard deviation" : standarddev, 
        "max": maxx, 
        "min" : minn, 
        "sum" : summ
    }
    return calculations