#Testando Lambda em uma soma
soma = lambda x, y : x + y
print(soma(4, 2))
print((lambda x, y : x + y)(1, 2))

#Filter em uma lista com valores
#Com números
lista1 = [10, 2, -1, 3, 5, -9, -11, 2]
a=list(filter(lambda x: x == 2, lista1))
print(a)

#Com Chars
lista2 = ["a", "b", "a","c", "a", "b", "b"]
b=list(filter(lambda x: x == "a", lista2))
c=list(filter(lambda y: y == "b", lista2))
print(b)
print(c)