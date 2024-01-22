class Vehicle:
    def __init__(self, fare):
        self.fare = fare

    def __add__(self, other):
        return self.fare + other.fare
    
    def __lt__(self, other):
        return self.fare < other.fare
        
bus= Vehicle(20)
car= Vehicle(30)

total_fare = bus + car
print(total_fare)

compare = bus < car
print(compare)