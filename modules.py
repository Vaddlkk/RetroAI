import random

def ints(numbers): #Ints Function
    adstring = "".join(map(str, numbers))
    digitsl = list(adstring)
    random.shuffle(digitsl)
    sstring = "".join(digitsl)
    number = int(sstring)
    return number
