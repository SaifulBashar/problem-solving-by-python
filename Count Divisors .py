l,r,k = input().split()
count = 0
for i in range(int(l),int(r)+1):
    if i%int(k)>0:
        pass
    elif i%int(k)==0:
        
        count +=1
print(count)
