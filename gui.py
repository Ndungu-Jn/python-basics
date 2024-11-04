#!/usr/bin/python3

print("[+]WELCOME MR.Robot")

def display():
    name=input("Enter your name: ")
    staff_id=input("Enter your staff id: ").split()
    gender=input("Enter your gender: ")
    hours_worked=int(input("Enter your hours worked: "))
    print()
    pay=hours_worked*23
    print("[+]RESULTS>>..>>")
    print(f"name: {name}")
    print(f"staff_id: {staff_id}")
    print(f"gender: {gender}")
    print(f"hours_worked: {hours_worked}")
    print(f"pay: {pay}")
    return

gameover=True
while gameover:
    display()
    print()
    print("[+]Good Bye!!")
    con=input("Do you want to continue? (y/n): ")
    if con=="n":
        gameover=False
