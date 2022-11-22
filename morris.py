
def sleep():
    status["sleepiness"] += 3
    status["thirsty"] += 5
    status["hunger"] += 2
    status["bank konto"] -= 1500
    status["whisky"] -= 2
    status["Gram Guld"] += 0.5



def dead():
    return status["sleepiness"] > 100 or status["thirsty"] > 100 or status["hunger"] > 100


status = {"turn": 0, "sleepiness": 0, "thirsty": 0, "hunger": 0, "whisky": 50, "Gram Guld": 0, "bank konto": 7500}

while not dead() and status["turn"] < 1000:
        status["turn"] += 1
        sleep()
        print(status)