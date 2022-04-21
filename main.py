import csv
import pandas as pd
import requests as req
import random
import mysql.connector
from mysql.connector import Error
from server import Account, Contact

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

#Méthode permettant de créer une base de données de base si elle n'existe pas
def checkDB():
    try:
        connexion = mysql.connector.connect(host=host,
                                             user=user,
                                             password=password)
        mySql_Query = """CREATE DATABASE IF NOT EXISTS IOTNotification"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        connexion.commit() 
        mySql_Query = """CREATE TABLE IF NOT EXISTS `IOTNotification`.`Accounts`(`email` VARCHAR(30) NOT NULL, `password` VARCHAR(100), PRIMARY KEY (`email`));"""
        cursor.execute(mySql_Query)
        connexion.commit() 
        mySql_Query = """CREATE TABLE IF NOT EXISTS `IOTNotification`.`Contacts`(`name` VARCHAR(20), `email` VARCHAR(30), `phone` VARCHAR(20), `id` BIGINT NOT NULL, PRIMARY KEY (`id`));"""
        cursor.execute(mySql_Query)
        connexion.commit() 
        mySql_Query = """INSERT INTO `IOTNotification`.`Accounts` (`email`) SELECT ('a.a@gmail.com') WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Accounts`)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Accounts` SET password = SHA('a') WHERE email = 'a.a@gmail.com';"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (1) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts`)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Harpageon', email = 'Harpagon@gmail.com', phone = '06 00 00 00 01' WHERE id = 1;"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (2) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts` WHERE id = 2)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Mariane', email = 'Mariane@gmail.com', phone = '06 00 00 00 02' WHERE id = 2;"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (3) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts` WHERE id = 3)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Cleante', email = 'Cleante@gmail.com', phone = '06 00 00 00 03' WHERE id = 3;"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (4) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts` WHERE id = 4)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Valere', email = 'Valere@gmail.com', phone = '06 00 00 00 04' WHERE id = 4;"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (5) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts` WHERE id = 5)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Elise', email = 'Elise@gmail.com', phone = '06 00 00 00 05' WHERE id = 5;"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """INSERT INTO `IOTNotification`.`Contacts` (`id`) SELECT (6) WHERE NOT EXISTS (SELECT * FROM `IOTNotification`.`Contacts` WHERE id = 6)"""
        cursor.execute(mySql_Query)
        connexion.commit()
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = 'Anselme', email = 'Anselme@gmail.com', phone = '06 00 00 00 06' WHERE id = 6;"""
        cursor.execute(mySql_Query)
        connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

#Méthode permettant de récupérer l'ensemble des comptes de la base de données
def getAllAccounts():
    try:
        accounts = []
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT * FROM Accounts"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        result = cursor.fetchall()
        for i in result:
            accounts.append(Account(i[0], i[1]))
        return accounts
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

#Méthode permettant de récupérer l'ensemble des contacts de la base de données
def getAllContacts():
    try:
        contacts = []
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT * FROM Contacts"""
        cursor = connexion.cursor()
        cursor.execute(mySql_Query)
        result = cursor.fetchall()
        for i in result:
            contacts.append(Contact(i[0], i[1], i[2], i[3]))
        return contacts
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

#Méthode permettant d'ajouter un nouveau compte à la base de données
def addNewAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM Accounts WHERE email = %s"""
        data = json_data['data']
        val = (data['email'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        if(result[0][0] == 0):
            mySql_Query = "INSERT INTO Accounts (email, password) VALUES (%s, SHA(%s))"
            val = (data['email'], data['password'])
            cursor.execute(mySql_Query, val)
            connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()
    #if post_data not in account_BDD:
        #account_BDD.append(post_data)
        #print("[+] Account added successfully !")
    #else:
        #print("[/!\] Email is already registered !")

#Méthode permettant de supprimer un compte de la base de données 
def removeAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM Accounts WHERE email = %s"""
        #data = json_data['data']
        #val = (data['email'],)
        val = (json_data['email'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        if(result[0][0] == 1):
            mySql_Query = "DELETE FROM Accounts WHERE email = %s"
            #val = (data['email'],)
            val = (json_data['email'],)
            cursor.execute(mySql_Query, val)
            connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()
    #for account in account_BDD:
        #if account['id'] == post_account_id:
            #account_BDD.remove(account)
            #print("[+] Account removed successfully !")
            #return
    #print("[/!\] Account to be removed not found !")

#Méthode permettant de modifier un compte de la base de données 
def modifyAccount(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """UPDATE `IOTNotification`.`Accounts` SET password = SHA(%s) WHERE email = %s;"""
        data = json_data['data']
        val = (data['password'], data['email'])
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        connexion.commit()
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
