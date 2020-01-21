num=int(input("dwse noumero"))
s= [int(x) for x in str(num)]
#print (s)
    
while len(s)!=1:
    num=num*3
    print ("epi tria kanei",num)
    num=num+1
    print ("syn ena kanei",num)
    s=[int(x) for x in str(num)]
    #print (s)
    b=0
    #print (len(s))
    for i in range(len(s)):
        b=b+s[i]
        num=b
    print ("to athroisma olwn twn psifiwn einai",num)
    s=[int(x) for x in str(b)]
    #print (s)
   
        
    
print ("menei o monopshfios arithmos",s)

    
        
        
        
    
    
    
