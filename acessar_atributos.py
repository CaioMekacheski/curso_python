t = {'a': 5}
print(t['a'])

class Teste:
    a = 5

y = Teste()
print(y.a)

print(getattr(y, 'a'))

a = setattr(y, 'a', 6)

print(y.a)
