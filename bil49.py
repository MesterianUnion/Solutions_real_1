class Bil:

    def __init__(self, hjul, hastighed, fartboder):

        self.hjul = hjul
        self.hastighed = hastighed
        self.fartboder = fartboder

    def drive(self):
        print("WROOOOOOOOM!")


bil1 = Bil(4, 165, 1)
bil2 = Bil(8, 108, 27)

print("Hjul:", bil1.hjul, "Max KM/t", bil1.hastighed, "Fartbøder", bil1.fartboder)
print("")
print("Hjul:", bil2.hjul, "Max KM/t", bil2.hastighed, "Fartbøder", bil2.fartboder)
bil1.drive()