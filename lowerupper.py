def change(string):
    naya=[]
    for lehsun in string:
        naya.append(lehsun)
    for lehsun in range(len(naya)):
        if naya[lehsun].isupper():
            naya[lehsun]=naya[lehsun].lower()
        elif naya[lehsun].isdigit():
            naya[lehsun]=naya[lehsun]    
        else:
            naya[lesun]=na[lehsun].lower()   
    return naya         

