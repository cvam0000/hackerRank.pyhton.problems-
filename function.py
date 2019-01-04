output=[100]
x=int(input())
def insert1(list):
    a=int(list[2])
    output[a]=list[1]
def remove(list):
    a=list[1]
    for lehsun in range(len(output)):
        if output[lehsun]==a:
            del output[lehsun]
            break
for lehsun in range(x):
    list=[i for i in input().split(" ")]
    if list[0]=='insert':
        insert1(list)
    if list[0]=='print':
        print(output)
    if list[0]=='remove':
        remove(list)
    if list[0]=='append':
        output.append(list[1])
    if list[0]=='pop':
        x=len(output)
        del output[x-1]
    if list[0]=='reverse':
        reverse(list)
    if list[0]=='sort':
        output.sort()
    del list
print(list)
