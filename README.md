# IOT Notifications System -  8INF912 - Special Topic in Computer Science II

A notification system in case of detection of abnormal behavior.

## Installation

## MySql - Database

Connector/Python installers in native package formats are available for Windows and Unix systems

Windows: MSI installer package

Linux: Yum repository for EL7 and EL8 and Fedora; RPM packages for Oracle Linux, Red Hat and SuSE; Debian packages for Debian and Ubuntu

macOS: disk image package with PKG installer

You may need root privileges to perform the installation operation.

Binary distributions that provide the C extension link to an already installed C client library provided by a MySQL Server installation. For distributions that are not statically linked, you must install MySQL Server if it is not already present on your system. To obtain it, go to the MySQL download site.

### `mysql-connector`

Installing Connector/Python with pip

Use pip to install Connector/Python on most operating systems:

``` MySQL connector
pip install mysql-connector-python
```

As the database is local, in the code on the main.py part of the backend, put your administrator credentials and the password to be able to create and connect to the database.

![image](https://user-images.githubusercontent.com/78219632/163748169-19349a02-5ec9-470c-975e-54e02b55d277.png)

## Node React - Front

Download the package manager [Node](https://nodejs.org/en/download/) to install the front.

It is recommended to install Yarn through the npm package manager, which comes bundled with Node.js when you install it on your system.

Once you have npm installed you can run the following both to install and upgrade Yarn.

``` Yarn
npm install --global yarn
```

## Python - Back

Files requirements :

- main.py

- python.py

- CSV files that contains sensor data (measured_data.csv)

Librairies requirements :

- mysql-connector-python 8.0.28

- pandas 1.4.1

- requests 2.27.1

- simplejson 3.17.6


Launch back http server :

``` 
python server.py
```
WARNING : server.py calls functions from main.py, so this file must me in the same directory

## Usage

## Front 

![powershell](/screenshots/Screenshot_3.jpg)

```powershell
# go into the front folder
cd api-front 

# download the packages
yarn

# run the front
yarn start
```
![login](/screenshots/Screenshot_1.jpg)

You can now connect to the application by entering your login details.

You can take the following accounts to test the application

![image](https://user-images.githubusercontent.com/78219632/164730031-0a2ef362-49b2-4222-8907-5c30e33e4b86.png)

This will redirect you to the following page

![contacts](/screenshots/Screenshot_2.jpg)

## Contributing
Antoine Delay - 
Alexandre Do Pham - 
Valentin Mellier 
