class Bil:

    def __init__(self, hjul, hastighed, fartboder):

        self.hjul = hjul
        self.hastighed = hastighed
        self.fartboder = fartboder

    def __repr__(self):
        return f"Bil: Hjul: {self.hjul} Max KM/t: {self.hastighed} Fartbøder: {self.fartboder}"

    def drive(self):
        print("WROOOOOOOOM!")


bil1 = Bil(4, 185, 0)
bil2 = Bil(0, 640, 97)

print(bil1)
print("")
print(bil2)
bil1.drive()