#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# functions

def sl(x, m, b):
    return m*x+b

def rsqrd(residuals, y):
    rsq = 1 - np.sum(np.square(residuals))/np.sum(np.square(y-np.mean(y)))
    return rsq

def genexpfunc(x, a, k, c):
    return c+a*np.exp(k*x)

def estk(x,y,n):
    maxx=np.max(x)
    estk = -n / maxx
    return estk

def csv2xy(fn):
    x = []
    y = []
    inf = open(fn)
    for line in inf:
        line = line.rstrip()
        la = line.split(',')
        x.append(float(la[0]))
        y.append(float(la[1]))
    inf.close()
    x=np.array(x)
    y=np.array(y)
    return x,y

def geninvertedexpfunc(x, a, k, c):
    return c+a*(1-np.exp(k*x))

# Brautigam laboratory thermal denaturation equation
def tdmodel(T, m1, b1, m2, b2, deltaH, TM, R=8.314):
    line1=m1*T+b1
    line2=m2*T+b2
    Q=np.exp(-deltaH/(R*T)*(1-T/TM))
    return (line1+line2*Q)/(1+Q)


# In[ ]:


# variables
basedir = os.getcwd()

