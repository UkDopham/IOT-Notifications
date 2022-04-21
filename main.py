import csv
import pandas as pd
import requests as req
import random
import mysql.connector
import time
from mysql.connector import Error
# #EMAIL BOT SENDER
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Email Account
email_sender_account = "smarthomeAlerte@gmail.com"
email_sender_username = "Smart Home"
email_sender_password = "alerte1234!"
email_smtp_server = "smtp.gmail.com"
email_smtp_port =587
recipient ="valentin.mellier3@gmail.com"
email_subject = "Smart Home - Notification"
email_body = "Hey, you got an alert !"

#########A METTRE POUR SE CONNECTER BASE DE DONNEES#######
host = 'localhost'
user = 'root'
password = 'root'
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
        mySql_Query = """CREATE TABLE IF NOT EXISTS `IOTNotification`.`Datas`(`id` BIGINT NOT NULL, `type` VARCHAR(20), `value` DOUBLE, PRIMARY KEY (`id`));"""
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

#Méthode permettant d'ajouter un nouveau contact à la base de données
def addNewContact(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM Contacts WHERE email = %s"""
        data = json_data['data']
        val = (data['email'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        mySql_Query = """SELECT id FROM Contacts ORDER BY ID DESC LIMIT 1"""
        cursor.execute(mySql_Query)
        cpt = cursor.fetchall()
        if(cpt == []):
            cpt = result
            cpt[0][0] = 0
        connexion.commit()
        if(result[0][0] == 0):
            mySql_Query = "INSERT INTO Contacts (name, email, phone, id) VALUES (%s, %s, %s, %s)"
            val = (data['name'], data['email'], data['phone'], cpt[0][0] + 1)
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
        
#Méthode permettant d'ajouter une nouvelle donnée à la base de données
def addData(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM Datas WHERE id = %s"""
        data = json_data['data']
        val = (data['id'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        mySql_Query = """SELECT id FROM Datas ORDER BY ID DESC LIMIT 1"""
        cursor.execute(mySql_Query)
        cpt = cursor.fetchall()
        if(cpt == []):
            cpt = result
            cpt[0][0] = 0
        connexion.commit()
        if(result[0][0] == 0):
            mySql_Query = "INSERT INTO Datas (id, type, value) VALUES (%s, %s, %s)"
            #val = (cpt[0][0] + 1, data['type'], data['value'])
            cursor.execute(mySql_Query, val)
            connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

#Méthode permettant de supprimer un contact de la base de données            
def removeContact(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """SELECT COUNT(*) FROM Contacts WHERE id = %s"""
        val = (json_data['id'],)
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        result = cursor.fetchall()
        connexion.commit()
        if(result[0][0] == 1):
            mySql_Query = "DELETE FROM Contacts WHERE id = %s"
            val = (json_data['id'],)
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

#Méthode permettant de modifier un contact de la base de données 
def modifyContact(json_data):
    try:
        checkDB()
        connexion = mysql.connector.connect(host=host,
                                             database='IOTNotification',
                                             user=user,
                                             password=password)
        mySql_Query = """UPDATE `IOTNotification`.`Contacts` SET name = %s, email = %s, phone = %s WHERE id = %s;"""
        data = json_data['data']
        val = (data['name'], data['email'], data['phone'], data['id'])
        cursor = connexion.cursor()
        cursor.execute(mySql_Query, val)
        connexion.commit()
    except Error as e:
        print("Erreur en essayant de connecter à la base de données", e)
    finally:
        if connexion.is_connected():
            cursor.close()
            connexion.close()

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



class Account : 
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Contact :
    def __init__(self, name, email, phone, id):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id    

#--------------------------------------------------------------------------------
#Second thread gestion des données capteurs - envoi d'une alerte par mail

def sendmail(server,measureAnalysed):
    print(f"Sending email to {recipient}")
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = recipient
    message['Subject'] = email_subject
    body=email_body+str("\r\n")+str(measureAnalysed[0][0])+ " sensor, critical value : "+str(measureAnalysed[0][1])
    message.attach(MIMEText (body, 'plain'))
    server.send_message(message)#All emails sent, log out.
    # server.quit()

def alert():
    #Initialisation connexion mail
    #login to email server
    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    server.starttls()
    server.login(email_sender_account,email_sender_password)


    valuemeasured = extractMeasuredValues("measured_data.csv")
    random.shuffle(valuemeasured)

    for elem in valuemeasured:
        measureAnalysed=analyseModule(elem)
        time.sleep(3)
        #Si mesure définit comme anormal ou ayant été détecté comme une anomalie, notifier
        if(measureAnalysed[1]!=0):
            sendmail(server,measureAnalysed)
