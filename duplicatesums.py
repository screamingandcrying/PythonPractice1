#given 3 integers, return their sums, but if there are duplicate values, don't count those in the sum
#complete the function as your answer

def duplicateSums(a, b, c):
    if a != b and b != c and a != c:
        return a + b + c
    elif a == b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b

print(duplicateSums(1,2,3))     #should return 6
print(duplicateSums(2,3,2))     #should return 3
print(duplicateSums(1,1,1))     #should return 0
