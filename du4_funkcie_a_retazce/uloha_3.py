def samohlaskovy(retazec):
    spolhlas = "q,w,r,t,z,p,s,d,f,g,h,j,k,l,x,c,v,b,n,m"
    for i in range(len(retazec)):
        if retazec[i] in spolhlas:
            return False
    return True
retazec = input("Zadaj retazec: ")
print(samohlaskovy(retazec))
