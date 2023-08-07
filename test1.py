a = [1, 2, 3]
b = a
b[2] = 100
print(a)

def trick(x=[]):
    x.append(1)
    return x


a = trick()
b = trick()
c = trick([])

print(a)
print(b)
print(c)
