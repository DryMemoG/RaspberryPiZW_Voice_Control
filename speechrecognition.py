import speech_recognition as SR
R = SR.Recognizer()
import pymysql
import serial, time
import os


#funcion de busqueda en MySql
def MySQL_buscar(sQuery):
    try:
        db = pymysql.connect("localhost","root", "","dbRaspberry")
        cursor = db.cursor()
        cursor.execute(sQuery)
        result = cursor.fetchall()
        print(result)
    except:
        print("Problemas de conexión")


with SR.Microphone() as source:
    print("Di algo: ")
    audio = R.listen(source)
    sQuery=""
    try:
        text = R.recognize_google(audio, language='es-MX')
        print("Has dicho: {}".format(text))
        arrayS = text.split(' ')
        #iniciamos con identificar un SELECT.
        if arrayS[0]=="selecciona" or arrayS[0]=="seleccionar":
            array2=["","","",""]
            array2[0] = "SELECT "
            if arrayS[1] =="todos" or arrayS[1]=="todo":
                array2[1] = "* "
            if arrayS[2]=="de" and arrayS[3]=="la" or arrayS[3]=="las":
                array2[2]= "FROM "
                array2[3]=arrayS[5]
            for i in range(0,len(array2)):
                sQuery=sQuery+array2[i]
            print(sQuery)
            MySQL_buscar(sQuery)
            #un select con Like para buscar cualquier comida
        elif arrayS[0]=="Busca" or arrayS[0]=="buscar":
            array2=["SELECT ","* ","FROM ","comida ","WHERE ","nombrecomida ","LIKE ",""]
            array2[7]="'%"+arrayS[1]+"%'"
            for i in range(0,len(array2)):
                sQuery=sQuery+array2[i]
            print(sQuery)
            MySQL_buscar(sQuery)
            #envia un 1 via serial para encender el led en el programa arduino
        elif arrayS[0]=="enciende" or arrayS[0]=="encender":
            arduino=serial.Serial("COM3",9600)
            time.sleep(2)
            arduino.write(b'1')
            arduino.close()
            #envia un 0 via serial para apagar el led en el arduino
        elif arrayS[0]=="apagar" or arrayS[0]=="apaga":
            arduino=serial.Serial("COM3",9600)
            time.sleep(2)
            arduino.write(b'0')
            arduino.close()
            #abre cualquier programa de windows
        elif arrayS[0]=="Abre":
            os.system("NOTEPAD.EXE")
        else:
            print("Amiguito, Habla claro.!!!")
        
        
    except:
        print("No te entiendo")