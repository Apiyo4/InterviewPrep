
"""
BDD
----
input                 output
[1,2,3, 4], 2         [1,2,4]                       
[1,2,3], 4             [1,2,3] 
[1,2,3,4,5], 0          [1,2,3,4,5]   
[1,2,3], 3              [2,3]
[1,2,3,4,5] , 2  get length 5,  5-2 = 3, remove the node after the third one
 f
 
   f   s
[1,2,3,4,None], 2 
     -   

Pseudo code
-----------
1. create a fxn removeKthNode that takes in head and k as parameters
2. create a var counter that at the end will give us the length
3. create a var pointer
4. loop through linked list and return the counter value
5. if the counter value - k >= 0
6.      loop through the linked list until counter - k
7.          then change the value it points to
8. return


1.create fxn
2. check if the length of nodelist is greater than or equals to k:
3. move s pointer k times, each time increasing the counter
4. if s is pointing at None  we want to change what the head is pointing to    
5. Else we loop until s.next becomes none each time incrementing both pointers
6. when s.next becomes none, we want to change the value of f to point to the value after whatever it was pointing to
7. if length of nodelist was  less than k then we just want to return the head
"""
# class ListNode(object):
#     def __init__(self, x):
#         self.value = x
#         self.next = None
# def removeKthNode(head, k):
#     counter = 0
#     counter1 = 0
#     pointer = head
#     while pointer:
#         counter += 1
#         pointer = pointer.next
#     if counter - k >= 0:
#         while counter1 < counter - k :
#             pointer.next = pointer.next.next
#     return head



def remove_Kth_from_end(head, k):
    leng  = 0
    counter = 0
    f =  head
    s = head
    while s :
        leng += 1
        s =  s.next
    if leng >= k:
        while counter <= k :
            s = s.next
            counter +=1
        if s is None:
            head.value = head.next.value
            head.next = head.next.next
        while s.next is not None:
            f =  f.next
            s =  s.next
        f.next = f.next.next
    return head








