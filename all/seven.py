"""
BDD
input                               behavior                        output
2, [[1,2]]                          1->2                               2
3, [[1,2], [2,3], [1,3]]            1->2, 1->3  2->3                    3
3, [[1,2], [2,3], [3, 1] ]          1-> 2, 2->3, 3->2                   -1
3, [[1,2], [2,3]]                   1->2, 2->3                          -1


3, [[1,2], [2,3], [1,3]]
trusting = [1,2, 1]             
trusted = [2, 3, 3]
d = {                       n - 1 = 2  d[key] = n-1, key if in trusting -1
    2: 1,
    3: 2
}


pseudocode

1.create fxn uncover_spy takes n, trust
2. split trust into 2: trusting and trusted
3.  create a dictionary
4.  add value for trusted as keys in my dictionary and it's value as the number of times the key occur in trusted
5.  check to see if n-1 is in the dictionary and if it is get the key and check if it's not in trusting
6.   if true then I return Key
7. else  I return -1 


"""

def uncover_spy(n, trust):
    trusting_list= []  
    trusted_list =  []
    d = {}
    for a in trust:
        trusting_list.append(a[0])
        trusted_list.append(a[1])
    
    for a in trusted_list:
        if d.get(a):
            d[a] +=1
        else:
            d[a] = 1

    for a in trusted_list:
        if d[a] == n-1 and a not in trusting_list :
            return a
    return -1

print(uncover_spy(3,[[1,2], [2,3], [3, 1] ]  ))

