l1=[]
n=int(input("enter the number of elements you want in list:"))
for i in range(0,n+1):
    ele=int(input())
    l1.append(ele)

for i in range(len(l1)):
    if l1[i]>=0:
        print(l1[i])
