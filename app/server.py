from flask import Flask, render_template, send_from_directory
from pymongo import MongoClient 

import os

#specifico i template per far capire a python dove siano i file HTML e CSS
app = Flask(__name__, template_folder='templates', static_folder='static')
#docker permette di usare il nome del servizio 'database' come hostname

mongoUri = os.environ.get("MONGO_URI", "mongodb://database:27017")
client = MongoClient(mongoUri)




#test di connessione
db = client.test_db


#servire la pagina principale
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    try:
        print("Connesso al database MongoDb con sucesso!")
        app.run(host="0.0.0.0", port=5000, debug=True)
       
    except Exception as e:
        print("Errore di connessione al database: {e}")
        
     #host 0.0.0.0 e fondamentale per docker
        app.run(host="0.0.0.0", port=5000, debug=True)
        
