#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 9 20:21:37 2020

@author: Vaishakh
"""

"""

The below differntiate() method takes a 2d list consisting of coefficient, 
power of sine function and power of cosine function in each list as a parameter.

For example: f=3*sin^2(x)cos^3(x)+4*sin^4(x)cos^2(x)
             parameter for this function would be
             [[3,2,3],[4,4,2]]
"""

import math

def _differentiate(f):
    
    coeff=f[0]
    m    =f[1] #power of sine function
    n    =f[2] #power of cosine function
    return [coeff*m,m-1,n+1],[-coeff*n,m+1,n-1]


def differentiate(f=[[],[]]):
    
    """

    Differentiation of a function
    
    Parameters
    ----------
    f : TYPE-> 2d list
        DESCRIPTION->list of lists consisting of coefficient, 
        power of sine function and power of cosine function
        The default is [[],[]].
        
    Returns
    -------
    TYPE->2d list
    DESCRIPTION->list of lists consisting of coefficient, 
    power of sine function and power of cosine function of the 
    resultant fuction.
    
    Example:
        
    >>from calculus.trigonometry import differentiate
    >>differentiate(f=[[3,2,3],[4,4,2]])
    [[6, 1, 4], [-9, 3, 2], [16, 3, 3], [-8, 5, 1]]
    
    """

    result=[]
    for i in f:
        for j in _differentiate(i):
            if j[0]!=0:  #ignoring whose coefficient is zero
                result.append(j)
    return result
    

def derivative_at_p(f=[[],[]],p=math.pi/2):
    """
    
    Derivative of a function at x=p

    Parameters
    ----------
    f : TYPE->2d list
        DESCRIPTION->list of lists consisting of coefficient, 
        power of sine function and power of cosine function of the 
        resultant fuction. 
        The default is [[],[]].
    p : TYPE->float
        DESCRIPTION->The point x=p at which the value of derivative
        is to be found out. 
        The default is math.pi/2.

    Returns
    -------
    TYPE->float
    DESCRIPTION->The value of derivative occured at x=p.
    
    Example:
        
    >>from calculus.trigonometry import derivative_at_p
    >>derivative_at_p(f=[[3,2,3],[4,4,2]],p=math.pi/2)
    5.0

    """
    result=0
    f_derivative=differentiate(f)
    for i in f_derivative:
        result+=i[0]*(math.sin(p)**i[1])*(math.cos(p)**i[2])
    return round(result)
    
    
def integrate(f):
    
    """
    Intergration is not included in this module due to complex integral results.

    """
    return ("Intergration is not included in this module due to complex integral results.")
