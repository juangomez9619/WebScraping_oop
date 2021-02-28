class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z): # Constructor
        self.name = z
        print(f'{self.name} constructed')
    
    
    def party(self):
        self.x += 1
        print(f"So far {self.name} has", self.x)


    def __del__(self):
        print('I am destructed', self.x)

''' Inheritance '''

class FootballFan(PartyAnimal):
    points = 0
   
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)
 

an = PartyAnimal('Lola')
an.party()

an = 42 #Object is destroyed

print(an)
j = FootballFan('Juan')
j.party() 

