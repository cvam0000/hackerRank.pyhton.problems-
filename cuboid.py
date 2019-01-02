x=int(input())
y=int(input())
z=int(input())
n=int(input())
if x>y and z>y:
	chotu=y
if y>x and z>x:
	chotu=x
else:
	chotu=z
xr=[]
yr=[]
zr=[]
result=[]
sub_result=[]
for lehsun in range (0,x):
	xr.append(lehsun)
for lehsun in range (0,y):
	yr.append(lehsun)
for lehsun in range (0,y):
	zr.append(lehsun)
for lehsun in range (0,chotu):
	a=xr[lehsun]
	b=yr[lehsun]
	c=zr[lehsun]
	if a+b+c != n:
		result.append(a,b,c)
print(result)		
