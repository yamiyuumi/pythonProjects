num=int(input("δωσε ενα νουμερο:"))
#ο χρηστης εισαγει ενα νουμερο και το προγραμμα φτιαχνει μια λιστα με το καθε
#ψηφιο του
s= [int(x) for x in str(num)]

#τριπλασιαζει τον αριθμο,προσθετει 1 και επειτα ολα του τα στοιχεια μαζι

num=num*3
print ("επί 3 κάνει:",num)
num=num+1
print ("συν 1 κάνει:",num)
s=[int(x) for x in str(num)]
b=0
for i in range(len(s)):
    b=b+s[i]
    num=b
print ("το άθροισμα όλων των ψηφίων είναι:",num)
s=[int(x) for x in str(b)]

#επαναλαμβανει τη διαδικασια μεχρι να μεινει μονοψηφιος αριθμος (το μηκος
#της λιστας να ειναι 1

while len(s)!=1:
    num=num*3
    print ("επί 3 κάνει:",num)
    num=num+1
    print ("συν 1 κάνει:",num)
    s=[int(x) for x in str(num)]
    b=0
    for i in range(len(s)):
        b=b+s[i]
        num=b
    print ("το άθροισμα όλων των ψηφίων είναι:",num)
    s=[int(x) for x in str(b)]
print ("μένει ο μονοψήφιος αριθμός:",s)

    
        
        
        
    
    
