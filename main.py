# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def addalistas(lista: list):
    print("lista : ")
    print(lista)
    listavacia = []
    for i in range(0, 5, 1):
        listavacia.append(int(input("Dame el valor nº:".format(i - 1))))
    print(listavacia)
    for i in range(0, 5, 1):
        print(listavacia[i])


def addatupla(tupla: tuple, num):
    listemp = list(tupla)

    listemp.append(num)

    tupla = tuple(listemp)
    return tupla


addalistas([1, 2, 3, 4, 5, 6, 7, 8, 9])
tupla = (23, 34, 65, 23, 44)
print(addatupla(tupla, input("Dame el valor para añadir a Tupla:")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
