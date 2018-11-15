a=int(input("input no of students"))
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
first=second=1000
for x in marks_sort:
	if x<first:
		second=first
		first=x
	elif x<second and x!=first:
		second=x
position=marks_sort.index(second)    
print(main_list[position][0])
