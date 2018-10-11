import numpy as np
import datetime
import time
import cv2
import os

cap = cv2.VideoCapture(0)
while True:

    datovalido2 = False
    i = 0
    peso = input("Peso: ")
    while datovalido2 == False:
        try:
            peso = peso.replace(",", ".")
            peso = peso.replace(".", "")
            peso = peso.replace("=", "")
            peso = float(peso)
            if peso != 0:
              datovalido2 = True
        except:
            print("Peso no ha sido reconocido como float o es igual a 0.")
            peso = input("Peso:")

    if peso != 0:
        listapesos = []
        for i in range(0,10):
            inputpeso = input("Peso de la comida: ")
            try:
                inputpeso = inputpeso.replace(",", ".")
                inputpeso = inputpeso.replace("=","")
                inputpeso = inputpeso[2:]
                inputpeso = float(inputpeso)
                listapesos.append(inputpeso)
            except:
                i -= 1
        floatpeso = float(max(set(listapesos), key=listapesos.count))
        print("El peso de la comida es de %.3f kg" % floatpeso)
        fichero = open("C:/Users/Usuario/PycharmProjects/kitchen_app/pesos.log", "a")
        fichero.write("Peso: %.3f medido el " % floatpeso)
        fichero.write("%s" % (datetime.datetime.now()))
        fichero.write("\n")
        fichero.close()
      #  cap = cv2.VideoCapture(0)
        ret,frame = cap.read()
        print(ret)
        #cv2.imwrite(("C:/Users/Usuario/Desktop/pyCharm/%s.jpg" % (datetime.datetime.now())),frame)
        hora = time.time()
        try:
            cv2.imwrite(("C:/Users/Usuario/Desktop/pyCharm/%s.jpg" % (hora)), frame)
        except:
            print("Se ha creado la imagen igualmente")
        #cv2.imshow("epppp.jpg", frame)
       # cv2.imwrite("C:/Users/Usuario/Desktop/pyCharm/pycharm.jpg", frame)
        fichero = open("C:/Users/Usuario/PycharmProjects/kitchen_app/pesos.log", "a")
        fichero.write("Ruta absoluta de la imagen: %s\n\n" % (os.path.abspath(("%s.jpg" % (hora)))))
        fichero.close()

       # cv2.waitKey()
        cv2.destroyAllWindows()

