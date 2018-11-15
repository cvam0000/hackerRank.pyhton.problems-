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
count=0
for x in marks_sort:
	if x<first:
		second=first
		first=x
	elif x<second and x!=first:
		second=x

result=[]
for x in range(a):
	if marks_sort[x]==second:
		count+=1
		result.append(x)

print(result)
#if count>1:  
#print(main_list[position][0])
