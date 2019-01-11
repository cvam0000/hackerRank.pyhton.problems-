def minion_game(string):
    e=[]
    for i in string:
        e.append(i)
    stuart=0
    kevin=0
    different=[]
    vov=['A' , 'E' , 'I' , 'O'  ,'U']
    for i in string:
        if i not in different:
            different.append(i)
    print (different)

    for i in different:
        if i in vov:




#def check(string):


s = input()
minion_game(s)
