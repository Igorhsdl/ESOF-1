#! python3

import re,os
i=0
searchregex = re.compile((input("Digite a regex a ser pesquisada: ")))
for file in os.listdir("./texts/"):
    if file.endswith(".txt"):
        with open("./texts/"+file) as f:
            for line in f.readlines():
                mo = searchregex.search(line)
                if(mo != None):
                    print("Encontrei: " + mo.group())
                    i+=1
if(i):
    print(" regex encontrada %d vezes" %(i) )
else:
    print(" nada encontrado ")
input()
