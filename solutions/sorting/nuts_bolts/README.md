# Nuts & Bolts

Nuts and Bolts problem is also known as **Lock and Key** or **Red and Blue Water Jugs** 
 problem. The task is to sort values in two arrays *N* and *B* with one constraint: the 
 values from the same array cannot be compared. E.g. value from array *N* can only be 
 compared to a value in array *B*. Arrays are of the same length and contain same elements
 but in different order. 
 
Sort both arrays *N* and *B* in place.

Example:
```
Input:
N = ['%', '#', '$', '^', '!', '@']
B = ['$', '^', '!', '#', '@', '%']
Output: N = B = ['!', '#', '$', '%', '@', '^'] 
```

###See code:
- [Solution](./__init__.py)
- [Test](./test.py)