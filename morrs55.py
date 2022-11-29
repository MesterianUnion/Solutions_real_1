class Morris:
    def work(self, sleep, eat, mine, buy_whisky, drink, Gold):
        self.sleep = sleep
        self.eat = eat
        self.mine = mine
        self.buy_whisky = buy_whisky
        self.drink = drink
        self.Gold = Gold

def sleep(): #sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
    status["sleepiness"] -= 10
    status["thirsty"] += 1
    status["hunger"] += 1
    status["whisky"] += 0
    status["Gold"] += 0


def eat(): #sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
    status["sleepiness"] += 5
    status["thirsty"] -= 5
    status["hunger"] -= 20
    status["whisky"] += 0
    status["Gold"] -= 2

def mine(): #sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
    status["sleepiness"] += 5
    status["thirsty"] += 5
    status["hunger"] += 5
    status["whisky"] += 0
    status["Gold"] += 5

def buy_whisky(): #sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
    status["sleepiness"] += 5
    status["thirsty"] += 1
    status["hunger"] += 1
    status["whisky"] += 1
    status["Gold"] -= 1


def drink(): #sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0
    status["sleepiness"] += 5
    status["thirsty"] -= 15
    status["hunger"] -= 1
    status["whisky"] -= 1
    status["Gold"] += 0

def dead():
    return status["sleepiness"] > 100 or status["thirsty"] > 100 or status["hunger"] > 100


status = {"turn": 0, "sleepiness": 0, "thirsty": 0, "hunger": 0, "whisky": 0, "Gold": 0}

while not dead() and status["turn"] < 1000:
    status["turn"] += 1
    if status["sleepiness"] >= 90:
        sleep()
    elif status["hunger"] >= 85:
        eat()
    elif status["thirsty"] >= 85 and not status["whisky"] >= 1:
        buy_whisky()
    elif status["thirsty"] >= 80 and status["whisky"] >= 1:
        drink()
    else:
        mine()
    print(status)

