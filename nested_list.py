a=int(input("input no of studenst"))
main_list=[]
marks_sort=[]
for x in range (a):
	small_list=[]
	name=input()
	marks=float(input())
	small_list.append(name)
	small_list.append(marks)
	marks_sort.append(marks)
	main_list.append(small_list)
	del(small_list)
first=second=0

for x in range (a):
	if x>first:
		second=first
		first=x
	elif x>second and x!=first:
			second=x


prit (first,second)    
print(main_list)
