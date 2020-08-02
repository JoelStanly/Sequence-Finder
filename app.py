sequence=[]
add=0
multi=1
flag=1
while(1):
    val=int(input("Enter the sequence value or enter -1 to exit\n"))
    if(val!=-1):
        sequence.append(val)
    else:
        break
length=len(sequence)-2
i=0
while(i<=length):
    while(1):
        val=multi*sequence[i]+add
        if(val==sequence[i+1]):
            break
        elif(val>sequence[i+1] and add==0):
            print("Not a sequence")
            flag=0
            break
        elif(val>sequence[i+1]):
            add=0
            multi+=1
            i=0
        elif(i!=0):
            i=0
            multi+=1
            add=0
        else:
            add+=1
    if(flag==0):
        break
    i+=1
if(flag==1):
    print("Sequence is")
    print(str(multi)+"X"+"+"+str(add))
    print("Next Value is")
    print((sequence[i]*multi)+add)