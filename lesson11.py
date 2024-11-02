# functions
import math

from datetime import date


def calc_area_triangle(b, h):
    area = 0.5 * b * h
    print(area)


def cal_area_circle(radius):
    area = math.pi * radius * radius
    area = round(area, 2)
    print("Arae of circle is", area, "cm^2")


def print_todays_date():
    today = date.today()
    print(today)


def add(*args):
    total = 0
    for num in args:
        total += num
    print("The total is", total)

def sayHi(name, age=21):
    print("Hello", name, "my age is ", age)





# use a function == calling it
calc_area_triangle(8, 12)
calc_area_triangle(40, 10)

print("........................")

triangles = [[12, 16], [8, 9], [6, 13], [16, 41], [31.5, 66.97]]
for triangle in triangles:
    calc_area_triangle(triangle[0], triangle[1])

cal_area_circle(76.22)
print_todays_date()

print(".................")

add(1,2,4)
add(1,2,3,4,5,6,7,8,9)

print(".....................")
sayHi("Mary")
sayHi("John", 24)
