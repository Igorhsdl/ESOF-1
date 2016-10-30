#! python3

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower()== 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower()== 'delete':
    del(mcbShelf[sys.argv[2]])
    
elif len(sys.argv) == 2: 

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':
        for key in mcbShelf:
            del(mcbShelf[key])
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()

#mc.bat save key - salva o conteúdo da clipboard como key
#mc.bat list -  retorna uma lista com todas keys salvas
#mc.bat key - copia o conteúdo da key para a clipboard
#mc.bat delete - apaga todas as keys
#mc.bat delete key - apaga somente key
