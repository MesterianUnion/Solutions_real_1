class Karakter:

    def __init__(self, navn, helbred, angrebs_styrke):
        self.navn = navn
        self.max_HP = helbred
        self.HP = helbred
        self.angrebs_styrke = angrebs_styrke

    def __repr__(self):
        return f"Superhelt: {self.navn=:11} {self.max_HP=:4} {self.HP=:4} {self.angrebs_styrke=:3}"

    def slag(self, andre):
        print("\n", self.navn, "slag", andre.navn, "for", self.angrebs_styrke, "skade", "\n")
        andre.get_slag(self.angrebs_styrke)

    def get_slag(self, angrebs_styrke):
        self.HP -= angrebs_styrke

    def get_healing(self, healing_styrke):
        self.HP += healing_styrke


class Healer(Karakter):

    def __init__(self, navn, helbred, healing_styrke):
        super().__init__(navn, helbred, 0)
        self.healing_styrke = healing_styrke

    def heal(self, andre):
        print("\n", self.navn, "heals", andre.navn, "for", self.healing_styrke, "skade", "\n")
        andre.get_healing(self.healing_styrke)


per1 = Karakter("Hørsholm Kommune", 97, 7)
per2 = Karakter("Rudersdal Kommune", 101, 25)
per3 = Healer("Doctor Toilet Brush", 99, 8)
print(per1)
print(per2)
print(per3)
per2.slag(per1)
print(per2)
per3.heal(per2)
print(per2)