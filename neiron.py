import random

def ints(numbers):
    adstring = "".join(map(str, numbers))
    digitsl = list(adstring)
    random.shuffle(digitsl)
    sstring = "".join(digitsl)
    number = int(sstring)
    return number

def neiron(name):
    lists = [random.randint(1, 100) for _ in range(1000)]
    item = 1
    items = len(lists)
    count = random.randint(item, 500)
    result = random.sample(lists, count)
    result2 = ints(result)
    result3 = bin(result2)
    result3 = result3[2:]
    print(name)
    print(result3)
    return result3
    #print(f"1: {result}\n2:{result2}\n3:{result3}\n4:{result4}")