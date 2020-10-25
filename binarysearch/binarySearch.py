"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search  algorithm to find if the target number is contained in the array and should return its index if it is, otherwise -1.
BDD
---
input                                                       output
[1, 5, 23, 111], 111                                            3
[1,2,3], 8                                                      -1
two pointers
                   s
        f        
        1, 5, 23, 111
        m =(1 +3)//2 =  2

pseudocode
1. create a fxn
2. loop through our array
3. find m index,
4. then we check if arr[m]  == target
5. if it is, we return it
6. else we check to see if it's less than
7. if it is less than then, we move the left pointer to m + 1 index
8. if it's more than, we move right pointer to m-1 index

"""
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
# def BinarySearch(arr, t):
    # f = 0
    # s = len(arr) - 0
    # m = 0
    # f_ans = 0
    # while arr:
    #     m = (f + s )//2 
    #     if arr[m] == t:
    #         f_ans = m
    #     elif arr[m] < t :
    #         f = m + 1
    #         continue
    #     elif arr[m] > t :
    #         s = m -1
    #         continue
    # return f_ans
print(binarySearch([1, 5, 23, 111], 111))