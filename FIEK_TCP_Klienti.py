import socket
from sys import *
import pickle
import time


serverName = "localhost"
serverPort = 13000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName, serverPort))
def main():
    print('UNIVERSITETI I PRISHTINES')
    print('HASAN PRISHTINA')
    print('Fakulteti i Inxhinierise Elektrike dhe Kompjuterike')
    print("Per te zgjedhur sherbimin shkruani fjalet:")
    print("IPADRESA, NUMRIIPORTIT, PRINTO, KOHA, LOJA, COUNT, GFC, OE, PERSHENDETJE, KONVERTO, PALINDROME, REVERSE\n")
    sheno = input("Ju lutem vendosni njeren nga komandat me larte: ")
    kerkesa = sheno.upper()

    while True:

        if kerkesa == 'IPADRESA':
            s.sendall(str.encode(kerkesa))
            rez = s.recv(128).decode('utf-8')
            print('IP ADRESA e juaj eshte: ' + rez)
            break
        elif kerkesa == 'PRINTO':
            s.sendall(str.encode(kerkesa))
            zgjedhja = input('Shkruani nje fjali:')
            s.sendall(str.encode(zgjedhja))
            rez = s.recv(128).decode('utf-8')
            print('Fjalia e dhene eshte:' + rez)
            break
        elif kerkesa == 'COUNT':
            s.sendall(str.encode(kerkesa))
            Zgjedhja = input('Shtypni fjalin tuaj: ')
            s.sendall(str.encode(Zgjedhja))
            rez = s.recv(128).decode('utf-8')
            print('Numri i bashtingelloreve dhe zanoreve ne fjaline e shtypur eshte: ' +rez)

            break
        elif kerkesa == 'EMRIIKOMPJUTERIT':
            s.sendall(str.encode(kerkesa))
            rez = s.recv(128).decode('utf-8')
            print('Emri juaj eshte: ' +rez)
            break
        elif kerkesa == 'NUMRIIPORTIT':
            s.sendall(str.encode(kerkesa))

            emriportit = str(serverPort)
            s.sendall(str.encode(emriportit))
            rez = s.recv(128).decode('utf-8')
            print('Porti juaj eshte: ' + rez)
            print(emriportit)
            break
        elif kerkesa == 'KOHA':
            s.sendall(str.encode(kerkesa))
            rez = s.recv(128).decode('utf-8')
            print(rez)
            break
        elif kerkesa =='LOJA':
            s.sendall(str.encode(kerkesa))
            rez = s.recv(128).decode('utf-8')
            print('Numrat random te gjeneruar jane:' +rez)
            break
        elif kerkesa == 'GFC':
            s.sendall(str.encode(kerkesa))
            nr1 = input("Sheno nr e pare :")
            s.sendall(str.encode(nr1))
            nr2 = input("Sheno nr e dyte : ")
            s.sendall(str.encode(nr2))
            rez = s.recv(128).decode('utf-8')
            print('Numri me i madhe i perbashket eshte: ' + rez)
            break
        elif kerkesa == 'REVERSE':
            s.sendall(str.encode(kerkesa))
            fjalia = input("Shkruani nje fjali per te kthyer fjaline reverse: ")
            s.sendall(str.encode(fjalia))
            rez = s.recv(128).decode('utf-8')
            print('Fjalia ' + rez[1:])
            break
        elif kerkesa == 'PALINDROME':
            s.sendall(str.encode(kerkesa))
            fjalia = input("Shkruani nje fjali per te testuar a eshte Palindrome: ")
            s.sendall(str.encode(fjalia))
            rez = s.recv(128).decode('utf-8')
            print('Fjalia ' + rez)
            break
        elif kerkesa == 'KONVERTO':
            s.sendall(str.encode(kerkesa))
            print('Ju mund te beni keto konvertime: \nKilowattToHorsepower  \ncmToFeet \nFeetToCm \nkmToMiles \nMileToKm \nHorsepowerToKilowatt \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons')
            metoda = input('Zgjedhni nje opsion: ')
            s.sendall(str.encode(metoda))
            sasia = input('Jepni numrin qe doni te konvertoni')
            s.sendall(str.encode(sasia))
            rez = s.recv(128).decode('utf-8')
            print('Madhesia e konvertuar: ' +rez)
            break
        elif kerkesa == 'PERSHENDETJE':
            s.sendall(str.encode(kerkesa))
            print('Ju lutem vendosni disa emra: ')
            emrat = [input('Emri1: '), input('Emri2: '), input('Emri3: ')]
            emrat = pickle.dumps(emrat)
            s.send(emrat)
            for i in range(3):
                rez = s.recv(128).decode('utf-8')
                rez1 = s.recv(128).decode('utf-8')

                print(rez)
                print(rez1)

            break
        elif kerkesa == 'OE':
            s.sendall(str.encode(kerkesa))
            vlera = input("Vendos numer qift apo tek: ")
            s.sendall(str.encode(vlera))
            rez = s.recv(128).decode('utf-8')
            print(rez)
            break
        else:
            s.sendall(str.encode(kerkesa))
            print('Ju lutem shenoni komanden e duhur')
            rez = s.recv(128).decode('utf-8')
            print(rez)
            break


if __name__ == "__main__":
    main()

    i = input("Deshironi te provoni perseri? ")
    vendimi = i.upper()
    if vendimi == 'PO':
        main()
    else:
        s.close()






