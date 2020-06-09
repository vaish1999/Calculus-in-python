#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 9 20:21:37 2020

@author: Vaishakh
"""

"""

The below differntiate() method takes an array of arrays consisting of coefficient, 
power of sine function and power of cosine function as a parameter.

For example: f=3*sin^2(x)cos^3(x)+4*sin^4(x)cos^2(x)
             parameter for this function would be
             [[3,2,3],[4,4,2]]
"""
def _differentiate(f):
    
    coeff=f[0]
    m    =f[1] #power of sine function
    n    =f[2] #power of cosine function
    return [coeff*m,m-1,n+1],[-coeff*n,m+1,n-1]


def differentiate(f):
    
    """

    Differentiation of a function
    
    Example:
        
    >>from calculus.trigonometry import differentiate
    >>differentiate([[3,2,3],[4,4,2]])
    [[6, 1, 4], [-9, 3, 2], [16, 3, 3], [-8, 5, 1]]
    
    """

    result=[]
    for i in f:
        for j in _differentiate(i):
            if j[0]!=0:  #ignoring whose coefficient is zero
                result.append(j)
    return result

def integrate(f):
    
    """
    Intergration is not included in this module due to complex integral results.

    """
    return ("Intergration is not included in this module due to complex integral results.")
