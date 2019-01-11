def minion_game(string):
    e=[]
    for i in string:
        e.append(i)
    stuart=[]
    kevin=[]
    different=[]
    vov=['A' , 'E' , 'I' , 'O'  ,'U']
    for i in string:
        if i not in different:
            different.append(i)
    print (different)




#def check(string):


s = input()
minion_game(s)
