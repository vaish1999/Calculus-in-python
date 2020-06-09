#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:10:53 2020

@author: Vaishakh
"""

"""

Both the functions take an array or list of coefficients 
of the the powers of x of the polynomial function as a parameter 
and return the list of coefficients of powers x of the resultant functions


"""

def differentiate(f):
    
    """

    Differentiation of a function
    
    Example:

    >>from calculus.polynomial import differentiate
    >>differentiate([5,3,4,1])
    [15,6,4]
 
    """

    f=f[::-1]
    result=[]
    for i in range(1,len(f)):
        coeff=i*f[i]
        result.append(coeff)
    return result[::-1]

def integrate(f):
    
    """

    Integration of a function

    Example:

    >>from calculus.polynomial import integrate
    >>integrate([5,3,4,1])
    [1.25, 1.0, 2.0, 1.0, 0]

    """

    f=f[::-1]
    result=[0]
    for i in range(len(f)):
        coeff=f[i]/(i+1)
        result.append(coeff)
    return result[::-1]
