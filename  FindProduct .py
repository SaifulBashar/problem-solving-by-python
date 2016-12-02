def a(case):
    arr = [int(i) for i in input().split()]
    answer = 1
    for i in range(case):
        answer = (answer*arr[i])%1000000007
    return answer

case = int(input())
print(a(case))
