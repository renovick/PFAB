#Programming for Absolute Beginners Homework 3A by Ross Novick
 
 
Bradys = ['Mike', 'Carol', 'Marsha', 'Jan', 'Cindy', 'Greg', 'Peter', 'Bobby', 'Alice']
print "The length of the Bradys list: ", len(Bradys)
numBradys = len(Bradys)
x = 0
while x  < numBradys:
        print Bradys[x]
        x = x + 1

#Sorted
Bradys.sort()
x = 0
while x < numBradys:
        print Bradys[x]
        x = x + 1

#For...In Loop
for brady in Bradys:
        print brady