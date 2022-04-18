import csv
import pandas as pd
import requests as req
import random
import mysql.connector
from mysql.connector import Error

#--------------------------------------------------------------------
# #EMAIL BOT SENDER
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# #Email Account
# email_sender_account = "smarthomeAlerte@gmail.com"
# email_sender_username = "Smart Home"
# email_sender_password = "alerte1234!"
# email_smtp_server = "smtp.gmail.com"
# email_smtp_port =587
# recipient ="valentin.mellier3@gmail.com"
# email_subject = "Smart Home - Notification"
# email_body = "Hey, you got an alert 2 !"

# #login to email server
# server = smtplib.SMTP(email_smtp_server,email_smtp_port)
# server.starttls()
# server.login(email_sender_account,email_sender_password)#For loop, sending emails to all email recipients
# print(f"Sending email to {recipient}")
# message = MIMEMultipart('alternative')
# message['From'] = email_sender_account
# message['To'] = recipient
# message['Subject'] = email_subject
# message.attach(MIMEText(email_body, 'plain'))
# print(message)
# server.send_message(message)#All emails sent, log out.
# server.quit()

#########A METTRE POUR SE CONNECTER BASE DE DONNEES#######
host = 'localhost'
user = 'root'
password = 'mdp'
##########################################################
#--------------------------------------------------------------------


#account_BDD=[]

#Méthode permettant de créer une base de données de base si elle n'existe pas en local
def checkDB():
    try:
        connexion = mysql.connector.connect(host=host,
                                             user=user,
                                             password=password)
        mySql_Query = """CREATE DATABASE IF NOT EXISTS IOTNotification"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        connexion.commit() 
        mySql_Query = """CREATE TABLE IF NOT EXISTS `IOTNotification`.`Users`(`email` VARCHAR(30), `password` VARCHAR(100), PRIMARY KEY (`email`));"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        connexion.commit() 
        mySql_Query = """INSERT INTO `IOTNotification`.`Users` (`email`) SELECT ('email@gmail.com') WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Users`)"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Users` SET password = SHA('test') WHERE email = 'email@gmail.com';"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

#Méthode permettant d'ajouter un compte dans la base de données
def addNewAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM USERS WHERE email = %s"""
        val = (json_data[0]['email'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        if(result[0][0] == 0):
            mySql_Query = "INSERT INTO USERS (email, password) VALUES (%s, SHA(%s))"
            val = (json_data[0]['email'], json_data[0]['password'])
            cursor = connexion.cursor()
            cursor.execute(mySql_Query, val)
            connexion.commit()
            print("[+] Account added successfully !")
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()
    # if json_data not in account_BDD:
    #     account_BDD.append(json_data)
    #     print("[+] Account added successfully !")
    # else:
    #     print("[/!\] Email is already registered !")

#Méthode permettant de supprimer un compte dans la base de données 
def removeAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM USERS WHERE email = %s"""
        val = (json_data[0]['email'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        if(result[0][0] == 1):
            mySql_Query = "DELETE FROM USERS WHERE email = %s"
            val = (json_data[0]['email'],)
            cursor = connexion.cursor()
            cursor.execute(mySql_Query, val)
            connexion.commit()
            print("[+] Account removed successfully !")
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()
    # for account in account_BDD:
    #     if account['id'] == post_account_id:
    #         account_BDD.remove(account)
    #         print("[+] Account removed successfully !")
    #         return
    # print("[/!\] Account to be removed not found !")

#Méthode permettant de modifier un compte dans la base de données
def modifyAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """UPDATE `IOTNotification`.`Users` SET password = SHA(%s) WHERE email = %s;"""
        val = (json_data[0]['password'], json_data[0]['email'])
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        connexion.commit()
        print("[+] Account modified successfully !")
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()


def sendDataToWebInterface(packet):
    url = 'http://127.0.0.1:8080/'
    myobj = "Status: "+str(packet[1])+" Type: "+str(packet[0][0])+" Value: "+str(packet[0][1])
    postRequest = req.post(url, data = myobj)

# def sendDataToMobilePhone(packet):

def extractMeasuredValues(filename):
    csvreader = pd.read_csv(filename,sep=';')
    rows = []
    for row in csvreader.values:   
        rows.append(row)
    return rows

#Définition des seuils
#GAZ, en volts (Entre 1 et 5)
#TEMP, en degré (Entre 10 et 30) capteur d'intérieur
#MOV, en m (Entre 3 et 10)
def analyseModule(data):
    #Status 0 : normal / 1 : detection / 2 : anomalie
    status=0
    #Mesure de gaz
    if(data[0]=="GAZ"):
        if(data[1]>0 and data[1]<1):
            return (data,status)
        elif(data[1]>=1 and data[1]<=3):
            status=1
            return (data,status)
        else:
            status=2
            return (data,status)
    #Mesure de température
    elif(data[0]=="TEMP"):
        if(data[1]>=10 and data[1]<=30):
            return (data,status)
        elif((data[1]<10 or data[1]>-5) or (data[1]>30 or data[1]<40)):
            status=1
            return (data,status)
        else:
            status=2
            return (data,status)    
    #Mesure de mouvement
    elif(data[0]=="MOV"):
        if(data[1]<=1 and data[1]>=0):
            return (data,status)
        elif(data[1]>=3 and data[1]<=10):
            status=1
            return (data,status)
        else:
            status=2
            return (data,status) 

# valuemeasured = extractMeasuredValues("measured_data.csv")
# random.shuffle(valuemeasured)

# for elem in valuemeasured:
#     measureAnalysed=analyseModule(elem)
#     #Si mesure définit comme anormal ou ayant été détecté comme une anomalie, notifier
#     if(measureAnalysed[1]!=0):
#         sendDataToWebInterface(measureAnalysed)
#         # sendDataToMobilePhone(measureAnalysed)




