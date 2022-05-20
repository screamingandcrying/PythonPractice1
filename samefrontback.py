#given a list of integers, return True if the length of the list is greater than 1 AND
#the first element and the last element are equal
#complete the function as your answer
def sameFrontBack(numbers):
    if len(numbers) > 1 and numbers[0] == numbers[len(numbers)-1]:
       return True
    else:
        return False

print(sameFrontBack([1,2,3]))              #should return False
print(sameFrontBack([1,2,3,1]))            #should return True
print(sameFrontBack([1,2,1]))              #should return True
print(sameFrontBack([1,2,3,4,5,6,7]))      #should return False
print(sameFrontBack([]))                   #should return False
print(sameFrontBack([1]))                   #should return False
