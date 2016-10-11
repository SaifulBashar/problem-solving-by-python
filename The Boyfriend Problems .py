case = int(input())
for i in range(case):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort(reverse=True)
    str1 = ''.join(str(e)+" " for e in arr)
    print(str1)
