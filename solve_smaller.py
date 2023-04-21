#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict


# In[ ]:


# solve a problem by solving smaller parts.
# In this example, return the smallest subset of Nums adding to K.
def solve(K, Nums):
    ks_to_solve = set([K])
    soln = defaultdict(list)
    while True:
        print(f"Yet to solve {ks_to_solve}")
        next_ks_to_solve = set()
        
        for k in ks_to_solve:
            if k in soln:
                print(f"{k} in soln")
                prev_soln = soln[K-k].copy()
                prev_soln += soln[k]
                soln[K] = prev_soln
                break
            for n in Nums:
                if k - n >= 0:
                    # we must have already solved (K - k).
                    prev_n = K-k
                    prev_soln = soln[prev_n].copy() # empty for prev_n=0
                    prev_soln += [n]
                    if (prev_n+n) in soln and len(soln[prev_n+n]) <= len(soln[prev_n]):
                        #print(f"{prev_n+n} in soln")
                        pass # we already have an equal or better solution
                    else:
                        print(f"adding {prev_n+n} to soln")
                        soln[prev_n+n] = prev_soln
                if n == k:
                    break # we found a solution which must also be the shortest
                if k > n:
                    next_ks_to_solve.add(k-n)
        
        if K not in soln and next_ks_to_solve:
            ks_to_solve = next_ks_to_solve
        else:
            break
    
    if K in soln:
        return soln[K]
    else:
        return []
                    


# In[ ]:


K=68
N=[1,14,17,38]
result = solve(K,N)

print(f"The smallest choice in {N} that sums to {K} is {result}")

