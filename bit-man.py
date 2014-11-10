
def SetBit(n, ind, b):
    if b:
        return (n | 1 << ind)
    else:
        # return (n & (~(0)))
        return (n & ~(1 << ind))


st = 23
print bin(st)[2:]
print bin(SetBit(st, 3, 1))[2:]
print bin(SetBit(st, 2, 0))[2:]

