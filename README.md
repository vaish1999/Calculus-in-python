# Calculus-in-python
Just differentiate and integrate!

Place the attached calculus folder in the directory /home/anaconda3/lib/python3.7/site-packages.

Yes,you are now ready to explore calculus in python.

Example 1:

```python
from calculus.polynomial import differentiate

differentiate(f=[5,3,4,1])
```

Output-

```python
[15,6,4]
```

Example 2:

```python
from calculus.polynomial import integrate

integrate(f=[5,3,4,1])
```

Output-

```python
[1.25, 1.0, 2.0, 1.0, 0]
```

Example 3:

```python
from calculus.trigonometry import differentiate

differetiate(f=[[3,2,3],[4,4,2]])
```

Output-

```python
[[6, 1, 4], [-9, 3, 2], [16, 3, 3], [-8, 5, 1]]
```

Example 4:

```python
from calculus.trigonometry import derivative_at_p

derivative_at_p(f=[[3,2,3],[4,4,2]],p=math.pi/2)
```

Output-

```python
0
```

