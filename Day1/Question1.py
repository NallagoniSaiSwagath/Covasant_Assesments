""" Given:D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
Create below:
 union of keys, #value does not matter
D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
 intersection of keys, #value does not matter
D_INTERSECTION = {'ok': 1}
D1- D2 = {'nok': 2 }
values are added for same keys
D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }

 """
D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
D_union={}
D_union=D1.copy()
for k,v in D2.items():
    if k not in D1:
        D_union[k]=v
print(D_union)

D_in={}
for k in D1:
    if k in D2:
        D_in[k]=D1[k]
print(D_in)

D_sub={}
D_sub = {k: D1[k] for k in D1 if k not in D2}
print(D_sub)

D_merge={}
D_merge=D1.copy()
for k in D2:
    if k in D1:
        D_merge[k]=D1[k]+D2[k]
    else:
        D_merge[k]=D2[k]
print(D_merge)