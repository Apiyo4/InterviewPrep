# Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to find if the target number is contained in the array and should return its index if it is, otherwise -1
# BDD
# input                                                                                   output
# [1, 5, 23, 111], 111)                                                                  3
# [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],70                                             -1              

# len = 10
# at len = 5 , 45 </> 70,less
# at len = 8 , 72 </>70 , greater than
# so we see if at -1 there is 70, if not we return -1

# pseudocode
# 1.create a fxn that takes in array and target integer
# 2. loop to 
def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
    if guess == item:
        return mid
    if guess > item:
        high = mid - 1
    else:
        low = mid + 1
    return None 
print(binary_search([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],70))