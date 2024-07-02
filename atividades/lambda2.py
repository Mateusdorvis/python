callables = []
a = ""
for i in (1, 2, 3): #a é igual a 1 e 2 e i é igual a 3
    callables.append(lambda a=i : a)

for f in callables:
    print(f())