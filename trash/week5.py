def AND(bit1, bit2):
    return bit1 == 1 and bit2 == 1


def OR(bit1, bit2):
    return bit1 == 1 or bit2 == 1

class Bite:
    def __init__(self, bits='0000'):
        self.val = bits

    def valToList(self):
        return [int(i) for i in self.val]

    @staticmethod
    def listToVal(bits):
        return ''.join([str(bit) for bit in bits])

    def count(self):
        bites = self.valToList()
        n = 0
        for i, bit in enumerate(bites):
            n += 8 if bit == 1 and i == 0 else 0
            n += 4 if bit == 1 and i == 1 else 0
            n += 2 if bit == 1 and i == 2 else 0
            n += 1 if bit == 1 and i == 3 else 0
        print(n)

    def add(self):
        bits = self.valToList()
        for i, bit in enumerate(bits[::-1]):
            i = len(bits) - i - 1
            if bit == 0:
                bits[i] = 1
                break
            else:
                bits[i] = 0
                if i > 0:
                    bits[i-1] = 1
        self.val = self.listToVal(bits)

    def sub(self):
        bits = self.valToList()
        for i, biti in enumerate(bits[::-1]):
            i = len(bits) - i - 1
            if biti == 1:
                bits[i] = 0
                for j, bitj in enumerate(bits[i:-1]):
                    if bitj == 0:
                        j = j + i + 1
                        bits[j] = 1
                break
        self.val = self.listToVal(bits)


def calcAdd(bites1, bites2):
    bite = Bite().valToList()
    for i, (bite1, bite2) in enumerate(zip(bites1, bites2)):
        if i != 0 and AND(bite1, bite2):
            print('hello')
            bite[i-1] = 1
            bite[i] = 0
            continue
        if OR(bite1, bite2):
            bite[i] = 1
    print(bite)


inp1 = Bite()
x = 2
inp2 = Bite()
y = 3
for n in range(x):
    inp1.add()
for n in range(y):
    inp2.add()
calcAdd(inp1.valToList(), inp2.valToList())
print(1==1 and 1==1)