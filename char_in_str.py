def most_frequent(s):
    mydict={}
    for i in s:
        if i in mydict:
            mydict[i]+=1
        else:
            mydict[i]=1
    for j in sorted (mydict):
        print(j+" = ",mydict[j])
#I'm unable to to sort the value part, I googled it , but i didnt understand 
#"   key=lambda x: x[1]   "  _____ this part.....
    
    
q=input("Please enter a string : ")
most_frequent(q)
