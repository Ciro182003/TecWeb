#immagine python
FROM python:3.11-slim

#crea cartella di lavoro
WORKDIR /app

#copia dipendenze e installazione
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copia il resto del codice
COPY app/ .

#avvio del server
CMD ["python", "server.py"]