def minion_game(string):
    e=[]
    for i in string:
        e.append(i)
    stuart=0
    kevin=0
    sub_strings1=[]
    sub_strings2=[]
    different=[]
    for i in string:
        if i not in different:
            different.append(i)
    print (different)
    sub_string(different)




def sub_string(different):
    vov=['A' , 'E' , 'I' , 'O'  ,'U']



#def check(string):


s = input()
minion_game(s)
