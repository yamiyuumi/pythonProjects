f = open("lekseis.txt", "r")
word_list=[word for line in f for word in line.split()]
a=[]
b=" "
print (word_list)
for x in (word_list):
    if len(x)>3:
        print(x[1:] + x[0] + "ay")
    else:
        print (x)
    
f.close()
