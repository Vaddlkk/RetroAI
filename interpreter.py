from neiron import neiron

def interpreter():
    r1 = neiron("r1")
    r2 = neiron("r2")
    r3 = neiron("r3")
    r4 = neiron("r4")
    r5 = neiron("r5")
    result = f"0b{r1}{r2}{r3}{r4}{r5}"
    return result