'''n = int(input())
count = 0
if n ==0:
    print(0)
else:
    while n >0:
        dig =n%10
        if dig%2!=0:
            count+=1
        n//=10
    print(count)'''


'''n = int(input())
count = 0
if n==0:
    print(0)
else:
    while n>0:
        dig = n%10
        count+=1
        n = n//10
    print(count)'''

'''n = list(map(int, input().split()))
key = 0
for i in range(0, len(n)):
    if n[i]> key:
        key = n[i]
print(key)'''

'''n = int(input())
key = 0
if n ==0:
    print(0)
while n>0:
    dig = n%10
    if dig> key:
        key = dig
    n//=10
print(key)'''

#amstrong of a number    153 =1^2 + 5^2 +3^2
n = int(input())
real = n
isNar = True
digits= len(str(n))
Sum = 0
if n<0:
    isNar = False
else:
    while n>0:
        dig = n%10
        Sum = dig**digits +Sum
        n//=10
if Sum==real:
    isNar=True
else:
    isNar=False
print(isNar)