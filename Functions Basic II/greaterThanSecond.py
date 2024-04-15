new_list = []
def greaterThan(lista):
    for i in lista:
        if i > lista[1]:
            new_list.append(i)
    print (len(new_list))
    return new_list
print(greaterThan([8,9,10,12,2,37,48,2,55]))