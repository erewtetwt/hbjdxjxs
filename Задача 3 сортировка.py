def main():
            
    def newMass():
        from random import randint
        m=[]
        len=int(input("Длина массива = "))
        for i in range(1,len+1):
            m.append(randint (1, 100))
        return(m)

    def Merge(M):
        if len(M)==1 or len(M)==0:
            return(M)
        LeftM=M[:len(M)//2]
        RightM=M[(len(M)//2):]
        #print(LeftM)
        #print(RightM)       
        return(AddMass(Merge(LeftM), Merge(RightM)))

    def AddMass(LM,RM):
        ResM=[]        
        while len(LM)!=0 and len(RM)!=0:
            if LM[0]<RM[0]:
                ResM.append(LM[0])
                del LM[0]
            else:
                ResM.append(RM[0])
                del RM[0]                
        if len(LM)==0:
            ResM.append(RM[0])
            #print(ResM)
        else:
            ResM.append(LM[0])
            #print(ResM)
        
        return (ResM)

    mass=newMass()
    print(mass)
    print("Done")
    print(Merge(mass))

main()
