#!/usr/bin/env python3
#program that receives a matrice and return the values from each column replaced by the values from each line

"""def printTable():
    col = int(input("quantas pessoas:"))
    running=True
    while running:"""
col = int(input())
matrice=[]
running=True
def print_table(mat):
    table_data = []
    for ind in range (len(mat[0])):
        newlin=[]

        for i in range (len(mat)):
            newlin.append(mat[i][ind])
        table_data.append(newlin)



    return table_data

while running:
    newline=[]
    for i in range (col):
        inf = input("type the inf: ")
        newline.append(inf)
    matrice.append(newline)
    ask = input("wanna continue?")
    if ask == 'no':
        running=False



tab = print_table(matrice)
for i in range (len(tab)):
    print(*tab[i])

