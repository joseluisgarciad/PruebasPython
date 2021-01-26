# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def listas(lista:list):
    print("lista1 : ")
    print(lista)
    Listavacia = []
    for i in range(0,5,1):
        Listavacia.append(int(input("Dame el valor nº:".format(i-1))))
    print(Listavacia)

    for i in range(0,5,1):
        print(Listavacia[i])

def Añadir_a_tupla(tupla:tuple, num):
    LisTemp = list(tupla)

    LisTemp.append(num)

    tupla=tuple(LisTemp)
    return tupla


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    listas([1, 2, 3, 4, 5, 6, 7, 8, 9])
    tupla=(23, 34, 65, 23, 44)
    print(Añadir_a_tupla(tupla, input("Dame el valor para añadir a Tupla:")))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
