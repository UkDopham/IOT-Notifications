from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
from numpy import mat
from main import addNewAccount,removeAccount
import simplejson

class Account : 
    def __init__(self, email, password):
        self.email = email
        self.password = password

# TODO get all accounts in database
a = Account("a.a@gmail.com", "a")
b = Account("b.b@gmail.com", "b")
c = Account("c.c@gmail.com", "c")

accounts = [ a, b, c]

class Contact :
    def __init__(self, name, email, phone, id):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id    

# TODO get contacts in database
d = Contact("Harpagon", "Harpagon@gmail.com", "06 00 00 00 01", 1)
e = Contact("Mariane", "Mariane@gmail.com", "06 00 00 00 02", 2)
f = Contact("Cleante", "Cleante@gmail.com", "06 00 00 00 03", 3)
g = Contact("Valere", "Valere@gmail.com", "06 00 00 00 04", 4)
h = Contact("Elise", "Elise@gmail.com", "06 00 00 00 05", 5)
i = Contact("Anselme", "Anselme@gmail.com", "06 00 00 00 06", 6)

contacts = [d, e, f, g, h, i]

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


    def do_GET(self):
        print("path is " + self.path)

        if self.path == "/api/get/allAccounts":
            print("api/get/allAccounts")
            #sendRespond(self, "api/get/allAccounts", 200)

            self._set_response()
            json_data = json.dumps([c.__dict__ for c in contacts])
            self.wfile.write(json_data.encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, DELETE, PUT')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_PUT(self):
        print("path is " + self.path)

        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, DELETE, PUT')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

        content_length = int(self.headers['Content-Length']) # Récupération taille de la requête
        post_data = self.rfile.read(content_length) # <--- Récupération des données
        json_data = simplejson.loads(post_data)

        if self.path == "/api/put/changeAccount":
            print("/api/put/changeAccount")
            # TODO Change account in database
            for contact in contacts :
                data = json_data['data']

                print(data)
                if contact.id == data['id']:                    
                    print("change " + contact.name)
                    contact.name = data['name']
                    contact.email = data['email']
                    contact.phone = data['phone']
                    break                   

            sendRespond(self, "api/put/changeAccount", 200)

        

    def do_DELETE(self):
        print("path is " + self.path)
        
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, DELETE')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

        content_length = int(self.headers['Content-Length']) # Récupération taille de la requête
        post_data = self.rfile.read(content_length) # <--- Récupération des données
        json_data = simplejson.loads(post_data)

        if self.path == "/api/delete":
            print("api/delete")
            print(json_data['id'])
            removeAccount(json_data['id'])
            sendRespond(self, "/api/delete", 200)


    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # Récupération taille de la requête
        post_data = self.rfile.read(content_length) # <--- Récupération des données
        json_data = simplejson.loads(post_data)

        # TODO Ajout d'un compte à la BDD
        print("path is " + self.path)

        if self.path == "/api/post/login":
            print("api/post/login")
            # TODO add check account
            print(json_data)
            
            isPossible = False

            for account in accounts :
                data = json_data['data']

                if account.email == data['email'] and account.password == data['password']:
                    isPossible = True
                    print("isPossible " + account.email)
                    break
            

            if isPossible : # if account exists
                sendRespond(self,"/api/post working", 200)
            else : 
                sendRespond(self, "/api/post error", 400)

            self._set_response()
            self.wfile.write("done".encode('utf-8'))

        elif self.path == "/api/post/newAccount":
            print("/api/post/newAccount")
            sendRespond(self,"/api/post working", 200)
            addNewAccount(json_data)
            id = "11" # TODO need to get id when adding in database    
            self._set_response()
            self.wfile.write(id.encode('utf-8'))   

        # logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #         str(self.path), str(self.headers), post_data.decode('utf-8'))
        

def sendRespond(self, msg, code):
        self.send_response(code, msg)


def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting BACKEND http server...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping BACKEND http server...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()