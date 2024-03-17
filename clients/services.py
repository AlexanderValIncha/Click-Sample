import csv
import os

from clients.models import Client

class ClientService:
    
    def __init__(self, table_name):
        self.table_name = table_name 
        
    def create_client(self,client):
        with open(self.table_name, mode='a') as f: 
            writer = csv.DictWriter(f, fieldnames=Client.schema()) 
            writer.writerow(client.to_dict()) 
            #Escribimos una nueva fila a nuestra estructura u objeto, necesitamos para DictWriter que nuestra entrada sea un diccionario .to_dict()
            
    
    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f,fieldnames=Client.schema())
            #reader es un iterable 
            return list(reader)
        

    def update_client(self,updated_client):
        clients = self.list_clients()
        
        updated_clients = []
        for client in clients:                      #ciclamos con un for a lo largo de los clientes
            if client['uid'] == updated_client.uid: #si nuestro cliente tiene el mismo id que el cliente que ha sido actualizado 
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)
                
        self._save_to_disk(updated_clients) #guardamos a disco generando una tabla temporal
      
    # Declaramos ahora una tabla temporal porque ya hemos abierto el archivo,
    # en el modo lectura con list_clients()     
    def _save_to_disk(self,clients): 
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f,fieldnames=Client.schema())
            writer.writerrows(clients)
            
    #finalmente nos falta renombrar esta tabla temporal al nombre de la tabla original
        os.remove(self.table_name)
        os.rename(tmp_table_name,self.table_name)