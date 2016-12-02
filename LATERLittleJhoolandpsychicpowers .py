import sys
def check(binary):
    l = list(binary)
    zero = 0
    one = 0
    for i in range(len(l)):
        if l[i] == '0':
            one = 0
            zero+=1
            if zero >= 6:
                return "Sorry, sorry!"
        elif l[i] == '1':
            zero = 0
            one+=1
            if one >= 6:
                return "Sorry, sorry!"
    return "Good luck!"

num = sys.stdin.read()
print(check(num))
