import re


def lunghezza(stringa):
    return len(stringa)


with open("prova.txt", "w") as myfile:
    myfile.write("Prova cacca, Pupu, popopopopop kono dio da")

with open("prova.txt", "r") as myfile2:
    lista1= []
    lunghezza1=[]
    string = myfile2.read()

    string = string.lower()

    string = re.sub(r"[^a-z]+", " ", string)

    lista = string.split()

    uni = [1] * len(lista)
    lunghezze=[]
    for i in lista:
        lunghezze.append(len(i))

    for index, i in enumerate(lista):
        presente= False
        for pos, k in enumerate(lista1):
            if i[0] == k[0]:
                presente= True
                lunghezza1[pos] += lunghezze[index]
                uni[pos] += 1
        if not presente:
            lista1.append(i)
            lunghezza1.append(len(i))
for i, a in enumerate(lista1):
    print("le parole con lettera ", a[0], "hanno lunghezza media:", lunghezza1[i]/uni[i])

