def coun(x):
    print(x)
def non():
    print('Too chaotic')
def last(x):
    return x[len(x)-1]   


def bribe(brr):
    count=0
    a=1
    for x in brr:
        for m in x:
            if m-a !=0 and m-a >0 and m-a <=3:
                count+=m-a
                if m==last(x):
                    coun(count)
            elif m-a >2:
                non()
            a+=1            
               
a=int(input())
brr=[[]]
for i in range(a):
    x=int(input())
    arr=[int(t) for t in input().split()]
    brr.append(arr)
bribe(brr)

