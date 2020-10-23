# 1.  create a fxn uncover_spy that takes in parameter n and array trust
def uncover_spy(n, trust):
# 2.  split trust into two: trusting_list and trusted_list
    trusting = []
    trusted = []
    for a in trust:
        trusting.append(a[0])
        trusted.append(a[1])
# 3. create a dict 
    d = {}
# 4. loop through trusted_list checking if it's in the dict, if it is add 1 to it otherwise let it's value be equal to 1
    for a in trusted:
        if d.get(a):
            d[a] += 1
        else:
            d[a] = 1
# 5. loop through to see if any of the keys has a value equals to n-1 and not in the trusting_list, if there is return the value

    for i in trusted:
        if  d[i] == n-1 and i not in trusting:
            return i

# 6. else return -1  
    return -1
print(uncover_spy(4,[[1, 3],[1, 4],[2, 3],[2, 4],[4, 3]] ))