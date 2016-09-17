# Nuts & Bolts

Nuts and Bolts problem is also known as **Lock and Key** or **Red and Blue Water Jugs** problem.
 The task is to sort values in two arrays *N* and *B* with one constraint. The values
 from the same array cannot be compared. Value from array *N* can only be compared to a
 value in array *B*. Arrays are of the same length and contain same elements but in
 different order. Sort arrays *N* and *B* in place.

Example:
```
Input:
N = ['%', '#', '$', '^', '!', '@']
B = ['$', '^', '!', '#', '@', '%']
Output: N = B = ['!', '#', '$', '%', '@', '^'] 
```