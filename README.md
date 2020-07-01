# Calculus-in-python
Just differentiate and integrate!

[![Downloads](https://pepy.tech/badge/pythcalculus)](https://pepy.tech/project/pythcalculus)

[![HitCount](http://hits.dwyl.com/vaish1999/Calculus-in-python.svg)](http://hits.dwyl.com/vaish1999/Calculus-in-python)

In this project, you will have one common parameter ie: 'f', which certainly means a function f(x).
In the polynomial part, f acts as a list of coefficients of decreasing powers of x in the function f(x). 
In the trigonometry part, f acts as a list of lists of coefficient, power of sine function and power of cosine function.


Example 1:  Differentiate f(x) = 5x <sup>3</sup> + 3x <sup>2</sup> + 4x + 1

```python
from calculus.polynomial import differentiate

differentiate(f=[5,3,4,1])
```

Output-

```python
[15,6,4]
```

Example 2: Integrate f(x) = 5x <sup>3</sup> + 3x <sup>2</sup> + 4x + 1

```python
from calculus.polynomial import integrate

integrate(f=[5,3,4,1])
```

Output-

```python
[1.25, 1.0, 2.0, 1.0, 0]
```

Example 3: Differentiate f(x) = 3sin<sup>2</sup>xcos<sup>3</sup>x + 4sin<sup>4</sup>xcos<sup>2</sup>x

```python
from calculus.trigonometry import differentiate

differetiate(f=[[3,2,3],[4,4,2]])
```

Output-

```python
[[6, 1, 4], [-9, 3, 2], [16, 3, 3], [-8, 5, 1]]
```

Example 4: Differentiate f(x) = 3sin<sup>2</sup>xcos<sup>3</sup>x + 4sin<sup>4</sup>xcos<sup>2</sup>x at x = 𝝿/2

```python
from calculus.trigonometry import derivative_at_p

derivative_at_p(f=[[3,2,3],[4,4,2]],p=math.pi/2)
```

Output-

```python
0
```


