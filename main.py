import os
import time


print('compilar programas com biblioteca SFML')
time.sleep(3)
os.system('cls')

mainCppLocal = input("diretorio arquivo fonte: ")
os.system('cls')
includeDirectory = input("\n\n qual o diretório de include do sfml?  ")
os.system('cls')
libDirectory = input("\n\n qual o diretório de libs do sfml? ")
os.system('cls')
debugOrRelease = input("\n\n debug ou release? d/r: ")
os.system('cls')
compileDebugMode = "g++ -I{} {} -L{} -lsfml-graphics-d -lsfml-window-d -lsfml-system-d".format(includeDirectory, mainCppLocal, libDirectory)
compileReleaseMode = "g++ -I{} {} -L{} -lsfml-graphics -lsfml-window -lsfml-system".format(includeDirectory, mainCppLocal, libDirectory)

if debugOrRelease == "d":
    os.system(compileDebugMode)
else:
    os.system(compileReleaseMode)

os.system('pause')