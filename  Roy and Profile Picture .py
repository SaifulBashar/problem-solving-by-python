l = int(input())
number = int(input())
for i in range(number):
    w,n = input().split()
    if int(w)<l or int(n)<l:
        print("UPLOAD ANOTHER")
    elif int(w) == l and int(n) == l or int(w) == int(n):
        print("ACCEPTED")
    elif int(w)>l or int(n)>l:
        print("CROP IT")
