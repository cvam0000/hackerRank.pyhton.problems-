bada_list=[]
chota_list=[]
result=[]
a=int(input())
m=0
list=[i for i in input().split(" ")]

for lehsun in range(int(input())):
        chota_list= [i for i in input().split(" ")]
        bada_list.append(chota_list)
        del chota_list


for lehsun in bada_list:
    for loda in range(a):
        if lehsun[0]==list[loda]:
            print(lehsun[1])
            result.append(int(lehsun[1]))
            list[loda]=0.1


print(sum(result))
