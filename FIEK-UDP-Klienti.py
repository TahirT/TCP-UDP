import socket
import pickle
from sys import *
serverName = "localhost"
serverPort = 13000
server_address = (serverName, serverPort)
client_address = (serverName, serverPort+1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((serverName, serverPort))
def main():
    print('UNIVERSITETI I PRISHTINES')
    print('HASAN PRISHTINA')
    print('Fakulteti i Inxhinierise Elektrike dhe Kompjuterike')
    print("Per te zgjedhur sherbimin shkruani fjalet:")
    print("IPADRESA, NUMRIIPORTIT, PRINTO, KOHA, LOJA, COUNT, GFC, PERSHENDETJE, KONVERTO, PALINDROME, REVERSE\n")
    sheno = input("Ju lutem vendosni njeren nga komandat me larte: ")
    kerkesa = sheno.upper()

    while True:

        if kerkesa == 'IPADRESA':
            s.sendto(str.encode(kerkesa),server_address)
            rez = s.recv(128).decode('utf-8')
            print('IP ADRESA e juaj eshte: ' + rez)
            break
        elif kerkesa == 'PRINTO':
            s.sendto(str.encode(kerkesa),server_address)
            zgjedhja = input('Shkruani nje fjali:')
            s.sendto(str.encode(zgjedhja),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Fjalia e dhene eshte:' + rez)
            break
        elif kerkesa == 'COUNT':
            s.sendto(str.encode(kerkesa),server_address)
            Zgjedhja = input('Shtypni fjalin tuaj: ')
            s.sendto(str.encode(Zgjedhja),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Numri i bashtingelloreve dhe zanoreve ne fjaline e shtypur eshte: ' +rez)

            break
        elif kerkesa == 'EMRIIKOMPJUTERIT':
            s.sendto(str.encode(kerkesa),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Emri juaj eshte: ' +rez)
            break
        elif kerkesa == 'NUMRIIPORTIT':
            s.sendto(str.encode(kerkesa),server_address)

            emriportit = str(serverPort)
            s.sendto(str.encode(emriportit),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Porti juaj eshte: ' + rez)
            print(emriportit)
            break
        elif kerkesa == 'KOHA':
            s.sendto(str.encode(kerkesa),server_address)
            rez = s.recv(128).decode('utf-8')
            print(rez)
            break
        elif kerkesa =='LOJA':
            s.sendto(str.encode(kerkesa),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Numrat random te gjeneruar jane:' +rez)
            break
        elif kerkesa == 'GFC':
            s.sendto(str.encode(kerkesa),server_address)
            nr1 = input("Sheno nr e pare :")
            s.sendto(str.encode(nr1),server_address)
            nr2 = input("Sheno nr e dyte : ")
            s.sendto(str.encode(nr2),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Numri me i madhe eshte: ' + rez[2:])
            break
        elif kerkesa == 'REVERSE':
            s.sendto(str.encode(kerkesa), server_address)
            fjalia = input("Shkruani nje fjali per te kthyer fjaline reverse: ")
            s.sendto(str.encode(fjalia), server_address)
            rez = s.recv(128).decode('utf-8')
            print('Fjalia ' + rez[1:])
            break
        elif kerkesa == 'PALINDROME':
            s.sendto(str.encode(kerkesa),server_address)
            fjalia = input("Shkruani nje fjali per te testuar a eshte Palindrome: ")
            s.sendto(str.encode(fjalia),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Fjalia ' + rez)
            break
        elif kerkesa == 'KONVERTO':
            s.sendto(str.encode(kerkesa),server_address)
            print('Ju mund te beni keto konvertime: \nKilowattToHorsepower  \ncmToFeet \nFeetToCm \nkmToMiles \nMileToKm \nHorsepowerToKilowatt \nDegreesToRadians \nRadiansToDegrees \nGallonsToLiters \nLitersToGallons')
            metoda = input('Zgjedhni nje opsion: ')
            s.sendto(str.encode(metoda),server_address)
            sasia = input('Jepni numrin qe doni te konvertoni')
            s.sendto(str.encode(sasia),server_address)
            rez = s.recv(128).decode('utf-8')
            print('Madhesia e konvertuar: ' +rez)
            break
        elif kerkesa == 'OE':
            s.sendto(str.encode(kerkesa),server_address)
            vlera = input("Vendos numer qift apo tek: ")
            s.sendto(str.encode(vlera),server_address)
            rez = s.recv(128).decode('utf-8')
            print(rez)
            break
        elif kerkesa == 'PERSHENDETJE':
            s.sendto(str.encode(kerkesa),server_address)
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
        else:
            s.sendto(str.encode(kerkesa), server_address)
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






