class Fligth():
    def __init__(self, capacity: int) -> None:
        self.capacityy = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacityy - len(self.passengers)


fligth = Fligth(3)
peoople = ["Heitor", "Maite","Arielle", "Jose", "Leticia"]

for person in peoople:
    if fligth.add_passenger(person):
        print(f"Added {person} to fligth Successfully!")
    else:
        print(f"Tickert Not Found! Sorry {person}")