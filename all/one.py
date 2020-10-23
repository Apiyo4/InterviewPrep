# 1.create fxn
def remove_kth_node_from_end(head, k):
# 2. check if the length of nodelist is greater than or equals to k:
    leng = 0
    f= head
    s= head
    counter = 0
    while s:
        leng +=1
        s= s.next
    if leng >= k:

# 3. move s pointer k times, each time increasing the counter
        while counter <= k:
            s= s.next
            counter += 1
# 4. if s is pointing at None  we want to change what the head is pointing to 
        if s is None:
            head.value = head.next.value
            head.next = head.next.next

# 5. Else we loop until s.next becomes none each time incrementing both pointers
        while s.next is not None:
            s =  s.next
            f = f.next
# 6. when s.next becomes none, we want to change the value of f to point to the value after whatever it was pointing to
        f.next = f.next.next
# 7. if length of nodelist was  less than k then we just want to return the head
    return head