import speech_recognition as SR
import pymysql
R = SR.Recognizer()


with SR.Microphone() as source:
    print("Di algo: ")
    audio = R.listen(source)
    sQuery=""
    try:
        text = R.recognize_google(audio, language='es-MX')
        #print("Has dicho: {}".format(text))
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
            for i in range(0,4):
                sQuery=sQuery+array2[i]
            print(sQuery)
        else:
            print("Select mal Redactado amiguito, Habla claro.")
        
        
    except:
        print("No te entiendo")


def mySql_Search(sQuery):
    db = pymysql.connect("localhost","root", "","dbRaspberry")
    cursor = db.cursor()
    cursor.execute(sQuery)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        






