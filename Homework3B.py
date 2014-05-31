#Programming for Absolute Beginners Homework 3B by Ross Novick
 
gpas = {"Lassoff" : 3.12, "Johnson" : 2.22, "Reich" : 3.59, "Honeychurch" : 2.98,
"Maini" : 3.11, "Levin" : 2.88, "Marcus" : 2.77, "Banks" : 3.71}
 
#Output key and value
for key,value in gpas.items():
         print "Last Name:", key, "      ", "GPA:", value
 
#Calculate the average GPA
average = 0
students = len(gpas)
for value in gpas.values():
         average = average + value
average = average/students
print "The average GPA of the class: ", average
 
#Output the class ranking
x = 1
while x <= len(gpas):
        for key in sorted(gpas, key=gpas.__getitem__, reverse=True):#sorts GPAs from high to low
                print "Rank #", x, "     ", key
                x = x + 1