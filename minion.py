
def score(a,b,string):
    count_kevin=0
    count_stuart=0
    c=0
    for lehsun in b:
        while lehsun in string[c:]:
            c=list[c:].find(lehsun)+1
            count_stuart+=1
            print (count_stuart)

    for lehsun in a:
        while lehsun in string[c:]:
            c=list[c:].find(lehsun)+1
            count_kevin+=1
            print (count_kevin)
            




def sep(list,vowels,string):
    vow=[]
    non=[]
    unique_list = []
    for el in list:
        if el not in unique_list:
            unique_list.append(el)
    
    for lehsun in unique_list:
        if lehsun[0] in vowels:
            vow.append(lehsun)
        else:
            non.append(lehsun)
    score(vow,non,string)



def minion_game(string):
    list=[]
    vowels=['A','E','I','O','u']
    vowel_in=[]
    for x in string:
        list.append(x)
        if x in vowels:
            vowel_in.append(x)
    print (list)
    print (vowel_in) 
    length = len(string)
    alist = []
    for i in range(length):
        for j in range(i,length):
            alist.append(string[i:j + 1]) 
    print(alist)        
    sep(alist,vowels,string)




              


s = input()
minion_game(s)




