f=open('tetrades2.txt','r')
#το πρόγραμμα δημιουργεί μια λίστα με κάθε γραμμή (κάθε τετράδα) του αρχείου
lineList = [line.rstrip('\n') for line in open("tetrades2.txt")]
#γεμίζει μια λίστα με 6 αριθμούς που εισάγει ο χρήστης με σειρά προτεραιότητας
a=[]
for j in range(6):
    o=int(input('δώσε αριθμό μεταξύ 1 και 9:'))
    a.append(o)
#δημιουργεί όλες τις πιθανές τετράδες των 6 αριθμών 
import itertools

for L in range(0, len(a)+1):
    for e in itertools.combinations(a, L):
        if len(e)==4:
            #ελέγχει κάθε στοιχείο της εξάδας με βαση τις τετράδες του αρχείου και αν
            #συμπληρωθεί τετράδα που υπάρχει στο αρχείο εμφανίζει κατάλληλο μήνυμα 
            sumb=0
            i=0
            while i<4:
                if str(e[i]) in lineList[0]:
                    sumb+=1
                i+=1
            if sumb == 4:
                print ("ο συνδιασμός",e,"δεν είναι διαθέσιμος")
            else:
                print ("μπορείτε να χρησιμοποιήσετε τον συνδιασμό",e)
            lineList=lineList[1:]

    

                
