
def check(word):
    mid = len(word)//2
    if word[:mid] == word[:-mid-1:-1]:
        print("YES")
    else:
        print("NO")

w  = input()
check(w)
