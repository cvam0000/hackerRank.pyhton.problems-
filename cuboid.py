x=int(input())
y=int(input())
z=int(input())
n=int(input())
result=[]
big=max(x,y,z)


def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:

        if value not in seen:
            output.append(value)
            seen.add(value)
    print(output)


def funky(a,b,c):
	for u in range (0,big):

		for lehsun in range (0,z+1):
			result.append([a,b,c])
			c+=1
		c=0
		for lehsun in range (0,y+1):
			result.append([a,b,c])
			b+=1
		b=0
		for lehsun in range(0,x+1):
			result.append([a,b,c])
			a+=1
		a=0

for o in range (0,big):
	funky(o,o,o)

result.sort()
g=remove_duplicates(result)
