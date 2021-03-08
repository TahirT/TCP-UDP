import socket
import datetime
import sys
import threading
from _thread import *
import random
import pickle
import time
import math
serverName = 'localhost'
serverPort = 13000

try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    print('Serveri eshte startuar ne localhost ne portin: ' + str(serverPort))
    serverSocket.listen(128)
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

    return bashtingllore -1, zanore

def EMRIIKOMPJUTERIT(): 
    return gethostname()

def KOHA():
    k = datetime.datetime.now()
    k = k.strftime('%H:%M:%S')
    return k

def LOJA():
    l = random.sample(range(0,49),7)
    
    numrin = str(l)
    return numrin

def KONVERTIMI(metoda, numri):
     if metoda == "KilowattToHorsepower":
        return numri*1.341

     elif metoda == "cmToFeet":
         return numri * 0.03280839895

     elif metoda == "FeetToCm":
         return numri * 30.48

     elif metoda == "kmToMiles":
         return numri * 0.62137119224

     elif metoda == "MileToKm":
         return numri * 1.609344

     elif metoda == "HorsepowerToKilowatt":
        return numri/1.341

     elif metoda == "DegreesToRadians":
        return numri*math.pi/180

     elif metoda == "RadiansToDegrees":
        return numri*180/math.pi

     elif metoda == "GallonsToLiters":
        return numri*3.785
     
     elif metoda == "LitersToGallons":
        return numri/3.785
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
def GFC(x, y):
    x=int(x)
    y=int(y)
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def HELLO(people):
    for person in people:
        x = "Pershendtje zotri/zonja " + person + ". Si jeni? "

        time.sleep(0.5)
        return x



def ID(people):
    i = 170714100120
    for person in people:
        z ="Qkemi! {}, ID-ja juaj eshte {}.".format(person, i)
        i += 1
        time.sleep(0.5)
        return z

def QiftTek(num):
    if (int(num) % 2) == 0:
        z = "{0} eshte Qift".format(num)
        return z
    else:
        z = "{0} eshte Tek".format(num)
        return z


def clientthread(lidhja):
    while True:
        try:
            zgjedhja = lidhja.recv(128).decode('utf-8')
            if not zgjedhja:
                break;


            komanda = str(zgjedhja)

            if komanda == 'IPADRESA':
                lidhja.send(str(IPADRESA()).encode('utf-8'))
            elif komanda == 'GFC':
                nr1 = lidhja.recv(128)
                nr2 = lidhja.recv(128)
                lidhja.send(str(GFC(nr1, nr2)).encode('utf-8'))
            elif komanda == 'REVERSE':
                fjalia = lidhja.recv(128)
                lidhja.send(str(REVERSE(fjalia)).encode('utf-8'))
            elif komanda == 'PALINDROME':
                fjalia = lidhja.recv(128)
                lidhja.send(str(PALINDROME(fjalia)).encode('utf-8'))

            elif komanda == 'NUMRIIPORTIT':
                lidhja.send(str(serverPort).encode('utf-8'))
            elif komanda == 'PRINTO':
                kerkesa = lidhja.recv(128)
                lidhja.send(kerkesa)
                lidhja.send(str(IPADRESA()).encode('utf-8'))
            elif komanda == 'COUNT':
                fjalia = lidhja.recv(128).decode('utf-8')
                print('Fjalia e dhene eshte: "'+str(fjalia)+'"')
                lidhja.send(str(BASHTINGLLORE(fjalia)).encode('utf-8'))

            elif komanda == 'EMRIIKOMPJUTERIT':
                lidhja.send(str(EMRIIKOMPJUTERIT()).encode('utf-8'))
            elif komanda == 'KOHA':
                lidhja.send((KOHA().encode('utf-8')))
            elif komanda == 'LOJA':
                lidhja.send((LOJA().encode('utf-8')))
            elif komanda == 'FIBONACCI':
                numri=lidhja.recv(128).decode('utf-8')
                print('Numri eshte: '+numri)
                nr=int(numri)
                lidhja.send(str(FIBONACCI(nr)).encode('utf-8'))
            elif komanda == 'KONVERTO':
                metoda = lidhja.recv(128).decode('utf-8')
                numri = lidhja.recv(128).decode('utf-8')
                nr = int(numri)
                print('Klienti ka zgjedhur te konvertoj' + str(metoda))
                lidhja.send(str(KONVERTIMI(metoda, nr)).encode('utf-8'))
            elif komanda == 'OE':
                num = lidhja.recv(128).decode('utf-8')
                lidhja.send(str(QiftTek(num)).encode('utf-8'))
            elif komanda == 'PERSHENDETJE':
                emrat = lidhja.recv(128)
                emri = pickle.loads(emrat)
                print('Emrat e vendosur jane: ' + str(emri))


                for person in emri:
                    x = "Pershendtje zotri/zonja " + person + ". Si jeni? "

                    time.sleep(0.5)
                    lidhja.send(str(x).encode('utf-8'))

                i = 170714100120
                for person in emri:
                    z = "Qkemi! {}, ID-ja juaj eshte {}.".format(person, i)
                    i += 1
                    time.sleep(0.5)
                    lidhja.send(str(z).encode('utf-8'))


            else:
                teksti = "Ju lutem shenoni komanda valide!"
                lidhja.send(str(teksti).encode('utf-8'))

        except IOError:
            print('ERROR')
            break

while 1:
    connection, address = serverSocket.accept()
    print("Serveri eshte i lidhur ne:" + str(address))
    start_new_thread(clientthread, (connection,))

serverSocket.close()

