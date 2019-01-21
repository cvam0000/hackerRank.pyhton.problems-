import re



def score(a,b,string):
    count_kevin=0
    count_stuart=0
    for lehsun in a:
        #print(string.count(lehsun))
        print(len(re.findall((lehsun), string)))
            




def sep(list,vowels):
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
    return vow ,non



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
    a,b=sep(alist,vowels)
    return a,b




              


s = input()
a,b=minion_game(s)
score(a,b,s)



