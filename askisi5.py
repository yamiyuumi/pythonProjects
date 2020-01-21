f = open("lekseis.txt", "r")

#το προγραμμα δημιουργει μια λιστα με καθε λεξη του κειμενου απο το αρχειο
word_list=[word for line in f for word in line.split()]


#για καθε λεξη του κειμενου,αν ειναι μεγαλυτερη απο 3 γραμματα τυπωνει την λεξη
#με το πρωτο της γραμμα στο τελος και το ay
#αλλιως τυπωνει την λεξη κανονικα
for x in (word_list):
    if len(x)>3:
        print(x[1:] + x[0] + "ay")
    else:
        print (x)
    
f.close()
