a=int(input("input no of studenst"))
main_list=[]
for x in range (a):
	small_list=[]
	name=input()
	marks=float(input())
	small_list.append(name)
	small_list.append(marks)
	main_list.append(small_list)
	del(small_list)

    
print(main_list)
