# MySql Information

Connector/Python installers in native package formats are available for Windows and Unix systems

Windows: MSI installer package

Linux: Yum repository for EL7 and EL8 and Fedora; RPM packages for Oracle Linux, Red Hat and SuSE; Debian packages for Debian and Ubuntu

macOS: disk image package with PKG installer

You may need root privileges to perform the installation operation.

Binary distributions that provide the C extension link to an already installed C client library provided by a MySQL Server installation. For distributions that are not statically linked, you must install MySQL Server if it is not already present on your system. To obtain it, go to the MySQL download site.

### `mysql-connector`

Installing Connector/Python with pip

Use pip to install Connector/Python on most operating systems:

pip install mysql-connector-python

As the database is local, in the code on the main.py part of the backend, put your administrator credentials and the password to be able to create and connect to the database.

