lista = []
def countdown(num):
    for i in range(num,0-1,-1):
        lista.append(i)
    return lista
print(countdown(15))