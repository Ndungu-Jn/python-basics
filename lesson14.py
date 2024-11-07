
class Criminal:
    def __init__(self, name, id_number, crime, gender):
        self.name = name
        self.id = id_number
        self.crime = crime
        self.gender = gender

    def show_details(self):
        print(f"Name: {self.name}\nId: {self.id}\nIssue: {self.crime}\nGender: {self.gender} ")

c1 = Criminal("Sinyonyo", "456", "stealing a girl", "M")
c1.show_details()