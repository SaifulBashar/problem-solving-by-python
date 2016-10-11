case = int(input())
for i in range(case):
    n = int(input())
    arr = list(input().split())
    arr = list(map(int,arr))
    
    print ("".join([str(x)+" " for x in arr] ))
    
    
