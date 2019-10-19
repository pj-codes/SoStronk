from itertools import combinations

arr=[('bleh',85),('Aequitas',90),('Aks',87),('Iam',20),('bill',50)]
m=2
combi=combinations(arr,m)
print(*combi)