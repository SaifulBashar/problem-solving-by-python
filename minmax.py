def output(l):

    m = min(l)
    minimum = m
    n = max(l)
    count = 0
    for i in range(len(l)):
        minimum += 1
        if minimum in l and minimum <= n:
            # print(minimum)
            count += 1
        elif minimum not in l and minimum <= n:
            return "NO"
    return "YES"

input()
l = [int(i) for i in input().split()]
print(output(l))
