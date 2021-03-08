import socket
import datetime
import sys
from _thread import *
import random
import math
import pickle
import time

serverName = 'localhost'
serverPort = 13000
server_address = (serverName, serverPort)

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(server_address)
    print('Serveri eshte startuar ne localhost ne portin: ' + str(serverPort))

    print('Serveri eshte duke pritur per ndonje kerkese')
except IOError:
    print("Lidhja nuk u formua")
    sys.exit()


def IPADRESA():
    return socket.gethostbyname(serverName)


def BASHTINGLLORE(x):
    zanore = 0
    bashtingllore = 0

    for i in x:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
                or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            zanore = zanore + 1
        else:
            bashtingllore = bashtingllore + 1

    return bashtingllore, zanore


def EMRIIKOMPJUTERIT():
    return gethostname()


def KOHA():
    k = datetime.datetime.now()
    k = k.strftime('%H:%M:%S')
    return k


def LOJA():
    l = random.sample(range(0, 49), 7)

    numrin = str(l)
    return numrin

def QiftTek(num):
    if (int(num) % 2) == 0:
        z = "{0} is Even".format(num)
        return z
    else:
        z = "{0} is Odd".format(num)
        return z
def KONVERTIMI(metoda, numri):
    if metoda == "KilowattToHorsepower":
        return numri * 1.341


    elif metoda == "HorsepowerToKilowatt":
        return numri / 1.341

    elif metoda == "cmToFeet":
        return numri * 0.03280839895

    elif metoda == "FeetToCm":
        return numri * 30.48

    elif metoda == "kmToMiles":
        return numri * 0.62137119224

    elif metoda == "MileToKm":
        return numri * 1.609344

    elif metoda == "DegreesToRadians":
        return numri * math.pi / 180

    elif metoda == "RadiansToDegrees":
        return numri * 180 / math.pi

    elif metoda == "GallonsToLiters":
        return numri * 3.785

    elif metoda == "LitersToGallons":
        return numri / 3.785
    else:
        return "Gabim"

def REVERSE(fjalia):
    txt = fjalia[::-1]
    return txt
def PALINDROME(fjalia):
    fjalia = fjalia.lower()

    rev_fjalia = reversed(fjalia)

    if list(fjalia) == list(rev_fjalia):
        return "Eshte palindrome"
    else:
        return "Nuk eshte palindrome."


def GFC(nr1, nr2):
    if nr1 > nr2:
        return nr1
    else:
        return nr2



while True:
    try:
        zgjedhja, from_address = serverSocket.recvfrom(128)
        zgjedhja = zgjedhja.decode()
        if not zgjedhja:
            break

        komanda = str(zgjedhja)

        if komanda == 'IPADRESA':
            serverSocket.sendto(str.encode(IPADRESA()),from_address)
        elif komanda == 'GFC':
                    nr1 = serverSocket.recvfrom(128)
                    nr2 = serverSocket.recvfrom(128)
                    serverSocket.sendto(str(GFC(nr1, nr2)).encode('utf-8'),from_address)
        elif komanda == 'PALINDROME':
                    fjalia = serverSocket.recv(128)
                    serverSocket.sendto(str(PALINDROME(fjalia)).encode('utf-8'),from_address)

        elif komanda == 'NUMRIIPORTIT':
                    serverSocket.sendto(str(serverPort).encode('utf-8'),from_address)
        elif komanda == 'PRINTO':
                    kerkesa = serverSocket.recv(128)
                    serverSocket.sendto(kerkesa,from_address)
                    serverSocket.sendto(str(IPADRESA()).encode('utf-8'),from_address)
        elif komanda == 'COUNT':
                    fjalia = serverSocket.recv(128).decode('utf-8')
                    print('Fjalia e dhene eshte: "' + str(fjalia) + '"')
                    serverSocket.sendto(str(BASHTINGLLORE(fjalia)).encode('utf-8'),from_address)

        elif komanda == 'EMRIIKOMPJUTERIT':
                    serverSocket.sendto(str(EMRIIKOMPJUTERIT()).encode('utf-8'),from_address)
        elif komanda == 'REVERSE':
            fjalia = serverSocket.recv(128)
            serverSocket.sendto(str(REVERSE(fjalia)).encode('utf-8'), from_address)
        elif komanda == 'KOHA':
                    serverSocket.sendto((KOHA().encode('utf-8')),from_address)
        elif komanda == 'LOJA':
                    serverSocket.sendto((LOJA().encode('utf-8')),from_address)
        elif komanda == 'FIBONACCI':
                    numri = serverSocket.recvfrom(128).decode('utf-8')
                    print('Numri eshte: ' + numri)
                    nr = int(numri)
                    serverSocket.sendto(str(FIBONACCI(nr)).encode('utf-8'),from_address)
        elif komanda == 'KONVERTO':
                    metoda = serverSocket.recv(128).decode('utf-8')
                    numri = serverSocket.recv(128).decode('utf-8')
                    nr = int(numri)
                    print('Klienti ka zgjedhur te konvertoj' + str(metoda))
                    serverSocket.sendto(str(KONVERTIMI(metoda, nr)).encode('utf-8'),from_address)
        elif komanda == 'OE':
            num = serverSocket.recv(128).decode('utf-8')
            serverSocket.sendto(str(QiftTek(num)).encode('utf-8'),from_address)
        elif komanda == 'PERSHENDETJE':
            emrat = serverSocket.recv(128)
            emri = pickle.loads(emrat)
            print('Emrat e vendosur jane: ' + str(emri))

            for person in emri:
                x = "Pershendtje zotri/zonja " + person + ". Si jeni? "

                time.sleep(0.5)
                serverSocket.sendto(str(x).encode('utf-8'),from_address)

            i = 170714100120
            for person in emri:
                z = "Qkemi! {}, ID-ja juaj eshte {}.".format(person, i)
                i += 1
                time.sleep(0.5)
                serverSocket.sendto(str(z).encode('utf-8'),from_address)

        else:
            tekst = "Gabim ju lutem vendosni komanda valide!"
            serverSocket.sendto(str(tekst).encode('utf-8'), from_address)


    except IOError:
            print('ERROR')
            break



