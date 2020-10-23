"""
BDD
---
input                       behavior                                                         output
2, [[1,2]]                 1=>2  but 2!=1, everyone trust spy                                   2
3, [[1,2], [1,3], [3,2]]    1=>2 and 3 => 2, 1=>3 but 2 doesn't    [1,1,3]  [2,3,2 ]                             2
3, [[1,3], [2,1], [3,2]]     1=>2 and 2=>1 and 3=>2, everyone trust each other  no spy [1,2,3][3,1,2]         -1
3, [[1,2], [2,3]]            1=>2 and 2=>3, no person is trusted by all hence no spy    [1,2] [2,3]        -1


set
Pseudocode
----------
1.  create a fxn uncover_spy that takes in parameter n and array trust
2.  split trust into two: trusting_list and trusted_list
3. create a dict 
4. loop through trusted_list checking if it's in the dict, if it is add 1 to it otherwise let it's value be equal to 1
5. loop through to see if any of the keys has a value equals to n-1 and not in the trusting_list, if there is return the value
6. else return -1

"""
def uncover_spy(n, trust):
    trusting_list = []
    trusted_list = []
    d = {}
    for a in trust:
        trusting_list.append(a[0])
        trusted_list.append(a[1])
    for b in trusted_list:
        if d.get(b):
            d[b] += 1
        else:
            d[b] = 1
    for c in trusted_list:
        if d[c] == n - 1  and c not in trusting_list :
            return c
    return -1   
    

print(uncover_spy(4,[[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]] ))