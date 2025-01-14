import random

async def coin():
    resalt = random.randint(1,2)
    if resalt == 1:
        otvet = 'Орёл'
    if resalt == 2:
        otvet = "Решко"
    return otvet
