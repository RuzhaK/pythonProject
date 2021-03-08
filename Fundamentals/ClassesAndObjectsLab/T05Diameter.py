class Circle:
    __pi=3.14
    def __init__(self,diameter):
        self.diameter=diameter
    def calculate_circumference(self):
        return self.diameter*self.__pi
    def calculate_area(self):
        return Circle.__pi*self.diameter/2*self.diameter/2
    def calculate_area_of_sector(self,angle):
        return (angle/360)*Circle.__pi*self.diameter/2*self.diameter/2
diameter=float(input())
angle=float(input())
circle=Circle(diameter)
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")