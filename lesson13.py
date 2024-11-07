# cylinder

class Cylinder:
    def __init__(self, radius, height, color):
        self.r = radius
        self.h = height
        self.c = color

    def calc_area(self, is_closed=True):
        if is_closed:
            area = 2 * 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            print(f"The area of closed cylinder is {area}")
        else:
            area = 22 / 7 * self.r ** 2 + 2 * 22 / 7 * self.r * self.h
            print(f"THe area of open cylinder is {area}")

    def calc_volume(self):
        v = 22 / 7 * self.r ** 2 * self.h
        print(f"The volume of cylinder is {v}")


c1 = Cylinder(10, 11, "red")
c2 = Cylinder(7.8, 24.6, "blue")
c1.calc_volume()
c1.calc_area(is_closed=False)
