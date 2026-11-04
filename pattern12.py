n = int(input())
start = 1 
for i in range(1,n):
    for j in range(0,i):
        print(start, end = " ")
        start= start+1
    print(" ")