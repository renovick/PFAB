#PFAB May 2014 Homework #4 by Ross Novick

class animal(object):
    'This class is designed to model real animals'
    
    def __init__(self, numberOfLegs, color, presenceOfFur, weight, length, species, name):
        self.numberOfLegs = numberOfLegs
        self.color = color
        self.presenceOfFur = presenceOfFur
        self.weight = weight
        self.length = length
        self.species = species
        self.name = name
        
    def sleep(self):
        print self.name, " the ", self.species, " is sleeping."
        
    def breathe(self):
        print self.name, " the ", self.species, " is breathing."
        
    def walk(self):
        print self.name, " the ", self.species, " is walking."
        
#Create an instance of animal that is a Dog
Dog = animal(4, "brown", "true", 24, 36, "canine", "Roofus")
Dog.sleep()
Dog.breathe()
Dog.walk()

#Create an instance of animal that is a Cat
Cat = animal(4, "grey", "true", 7, 27, "feline", "Mischief")
Cat.sleep()
Cat.breathe()
Cat.walk()
    
    
    