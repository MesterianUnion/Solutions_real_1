class Bil:

    def __init__(self, hjul, hastighed, fartboder):
        self.hjul = hjul
        self.hastighed = hastighed
        self.fartboder = fartboder

    def __repr__(self):
        return f"Hjul: {self.hjul} Max KM/t: {self.hastighed} Fartbøder: {self.fartboder}"

    def drive(self):
        print("RHHWROOROOROROOOUO")


class Ebil(Bil):

    def __init__(self, hjul, hastighed, fartboder, batteri):
        super().__init__(hjul, hastighed, fartboder)
        self.batteri = batteri

    def __repr__(self):
        return f"Hjul: {self.hjul} Max KM/t: {self.hastighed} Fartbøder: {self.fartboder} kW Batteri: {self.batteri}"

    def drive(self):
        print("Hiihihihiihihihihihhhh")


bil1 = Bil(4, 190, 0)
ebil = Ebil(4, 205, 4, 210)

print(bil1)
bil1.drive()
print("")
print(ebil)
ebil.drive()
print("")
print("")

# Ved ikke om jeg skulle lave et loop, men du har jeg lavet et. For
# En sikkerheds skyld. :)

print("Et loop:")
biler = [bil1, ebil]
for bil in biler:
    bil.drive()
