#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# functions

# the equation of a straight line
def sl(x, m, b):
    return m*x+b

# a general exponential function
# requires numpy
def genexpfunc(x, a, k, c):
    return c+a*np.exp(k*x)

# as used in this work, an exponential
# decay function with an inital value less than
# the final value; requires numpy
def geninvertedexpfunc(x, a, k, c):
    return c+a*(1-np.exp(k*x))

# the Brautigam laboratory protein thermal denaturation fit equation
# requires numpy
def tdmodel(T, m1, b1, m2, b2, deltaH, TM, R=8.314):
    line1=m1*T+b1
    line2=m2*T+b2
    Q=np.exp(-deltaH/(R*T)*(1-T/TM))
    return (line1+line2*Q)/(1+Q)

# a function which computes R-squared given numpy y and residuals vectors
def rsqrd(residuals, y):
    rsq = 1 - np.sum(np.square(residuals))/np.sum(np.square(y-np.mean(y)))
    return rsq

# a function to read x,y data from a csv file and
# return numpy vectors x and y
# requires numpy
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


# In[ ]:


# variables
basedir = os.getcwd() # or edit as you prefer

