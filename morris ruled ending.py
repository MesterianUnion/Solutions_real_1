def sleep():
    status["sleepiness"] -= 100
    status["thirsty"] += 50
    status["hunger"] += 33


def eat():
    status["hunger"] -= 33.5
    status["thirsty"] -= 28
    status["thirsty"] += 1


def mine():
    status["sleepiness"] += 25
    status["thirsty"] += 5
    status["hunger"] += 50
    status["whisky"] -= 0
    status["Gold"] += 4
    status["whisky"] -= 5


def buy_whisky():
    status["whisky"] += 5
    status["sleepiness"] += 75
    status["hunger"] -= 16
    status["thirsty"] -= 1


def dead():
    return status["sleepiness"] > 100 or status["thirsty"] > 100 or status["hunger"] > 100


status = {"turn": 0, "sleepiness": 0, "thirsty": 0, "hunger": 0, "whisky": 10, "Gold": 0}

while not dead() and status["turn"] < 1000:
    status["turn"] += 1
    sleep()
    eat()
    mine()
    buy_whisky()
    eat()
    print(status)
