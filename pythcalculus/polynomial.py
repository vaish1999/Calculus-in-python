#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:10:53 2020

@author: Vaishakh
"""


def differentiate(f=[]):
    """

    Differentiation of a function
    
    Parameters
    ----------
    f : TYPE->list
        DESCRIPTION->list of coefficients with decreasing powers of x.
        The default is [].

    Returns
    -------
    TYPE->list
    DESCRIPTION->lsit of coefficients of resultant function

    
    Example:

    >>from calculus.polynomial import differentiate
    >>differentiate(f=[5,3,4,1])
    [15,6,4]
 
    """

    f=f[::-1]
    result=[]
    for i in range(1,len(f)):
        coeff=i*f[i]
        result.append(coeff)
    return result[::-1]

def derivative_at_p(f=[],p=1):
    
    """

    Derivative of a function at x=p
    
    Parameters
    ----------
    f : TYPE->list
        DESCRIPTION->list of coefficients with decreasing powers of x.
        The default is [].
    a : TYPE->float
        DESCRIPTION->lower limit of the definite integral
        The default is 0.
    b : TYPE->float
        DESCRIPTION->upper limit of the definite integral
        The default is 1.

    Returns
    -------
    TYPE->float
    DESCRIPTION->The value of derivative occured at p.

    Example:

    >>from calculus.polynomial import derivative_at_p
    >>derivative_at_p(f=[5,3,4,1],p=2)
    76

    """
    
    f_derivative=differentiate(f)[::-1]
    result=0
    for i in range(len(f_derivative)):
        result+=f_derivative[i]*(p**i)
    return result

def integrate(f=[]):
    """
    Integration of a function

    Parameters
    ----------
    f : TYPE->list
        DESCRIPTION->list of coefficients with decreasing powers of x.
        The default is [].

    Returns
    -------
    TYPE->list
    DESCRIPTION->lsit of coefficients of resultant function

    
    Example:

    >>from calculus.polynomial import integrate
    >>integrate(f=[5,3,4,1])
    [1.25, 1.0, 2.0, 1.0, 0]
    
    """

    f=f[::-1]
    result=[0]
    for i in range(len(f)):
        coeff=f[i]/(i+1)
        result.append(coeff)
    return result[::-1]

def definite_integral(f=[],a=0,b=1):
    """
    Definite integral of a function between the limits a and b.

    Parameters
    ----------
    f : TYPE->list
        DESCRIPTION->list of coefficients with decreasing powers of x.
        The default is [].
    a : TYPE->float
        DESCRIPTION->lower limit of the definite integral
        The default is 0.
    b : TYPE->float
        DESCRIPTION->upper limit of the definite integral
        The default is 1.

    Returns
    -------
    TYPE->float
    DESCRIPTION->The value of Definite integral occured between
    the limits a and b.


    """
    
    f_integrate=integrate(f)[::-1]
    result=0
    for i in range(len(f_integrate)):
        result+=f_integrate[i]*(b**i-a**i)
    return result
    
