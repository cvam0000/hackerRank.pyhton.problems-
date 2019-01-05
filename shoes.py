bada_list=[]
chota_list=[]
result=[]
a=int(input())
list=[i for i in input().split(" ")]

for lehsun in range(int(input())):
        chota_list= [i for i in input().split(" ")]
        bada_list.append(chota_list)
        del chota_list


for lehsun in bada_list:
    for loda in list:
        if lehsun[0]==loda:
            result.append(int(lehsun[1]))
            del loda
print(sum(result))
