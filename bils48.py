
class Bil:

    def drive(self):
        print("WHRIIIIRRHMM")

car1 = Bil()
car1.hjul = 2
car1.fartboder = 3
car1.max_hastighed = 46


class Bil1:

    def drive(self):
        print("WHROOOORROROHOROROHHH")

car2 = Bil1()
car2.hjul = 4
car2.fartboder = 1
car2.max_hastighed = 290

print("Hjul:", car1.hjul, "Fartbøder:", car1.fartboder, "Max KM/t", car1.max_hastighed, "Køretøj: Cykel fra irma")
car1.drive()
print(" ")
print("Hjul:", car2.hjul, "Fartbøder:", car2.fartboder, "Max KM/t", car2.max_hastighed, "Køretøj: Racerbil")
car2.drive()